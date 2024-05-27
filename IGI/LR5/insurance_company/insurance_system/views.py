import logging

from django import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from company_info.models import PromoCode, Review
from insurance_system.forms import ContractForm, AgentsFilterForm, ContractsFilterForm
from insurance_system.models import ClientContract, Branch, Agent, InsuranceType

import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from statistics import mean, median, mode

logger = logging.getLogger(__name__)


@staff_member_required
def view_contracts(request):
    agent_contracts = []
    try:
        if request.user.employee is not None and request.user.employee.agent is not None:
            contracts = request.user.employee.agent.insurancecontract_set.all()
            logger.info("Contracts retrieved for agent: %s", request.user.employee.agent)
            for c in contracts:
                agent_contracts.extend(ClientContract.objects.filter(contract=c).all())
    except Exception as e:
        logger.error("Error retrieving contracts: %s", str(e))
        return render(request, "404.html")
    logger.info("Number of agent contracts found: %d", len(agent_contracts))
    return render(request, "view_contracts.html", {"contracts": agent_contracts})


@login_required
def profile(request):
    try:
        client = request.user.client
        contracts = ClientContract.objects.filter(client=client)
        logger.info("Contracts retrieved for client: %s", client)
    except Exception as e:
        logger.error("Error retrieving client profile: %s", str(e))
        return render(request, '404.html')
    return render(request, 'profile.html', context={'client': client, "contracts": contracts})


@login_required
def new_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            try:
                client_contract = form.save(commit=False)
                if isinstance(form.cleaned_data['promocode'], str) and form.cleaned_data['promocode'] != "":
                    client_contract.discount = PromoCode.objects.filter(
                        code=form.cleaned_data['promocode']).first().discount
                if isinstance(form.cleaned_data['promocode'], forms.ValidationError):
                    logger.warning("Invalid promocode provided: %s", form.cleaned_data['promocode'])
                    return render(request, "make_contract.html", {"form": form})
                client_contract.client = request.user.client
                client_contract.end_date = form.cleaned_data['start_date'] + client_contract.contract.duration
                client_contract.agents_salary = float(
                    1 - (0 if client_contract.discount is None else client_contract.discount) / 100) * float(
                    client_contract.contract.traffic_rate) * float(
                    client_contract.contract.insurance_type.commission_rate) * float(client_contract.insurance_amount)
                client_contract.save()
                logger.info("New contract created for client: %s", client_contract.client)
                return redirect("profile")
            except Exception as e:
                logger.error("Error creating new contract: %s", str(e))
                return render(request, "make_contract.html", {"form": form})
    else:
        form = ContractForm()
    return render(request, "make_contract.html", {"form": form})


def filials(request):
    if not request.user.is_superuser:
        logger.warning("Non-superuser attempted to access filials.")
        return redirect("404.html")
    filials_obj = Branch.objects.all()
    logger.info("Retrieved all filials.")
    return render(request, "super-filials.html", {"branches": filials_obj})


def contracts(request):
    if not request.user.is_superuser:
        logger.warning("Non-superuser attempted to access contracts.")
        return redirect("404.html")

    form = ContractsFilterForm(request.GET or None)

    if form.is_valid():
        cd = form.cleaned_data
        query = ClientContract.objects.all()
        if cd['branch']:
            query = query.filter(contract__agent__branch=cd['branch'])
            logger.info("Contracts filtered by branch: %s", cd['branch'])
        if cd['agent']:
            query = query.filter(contract__agent=cd['agent'])
            logger.info("Contracts filtered by agent: %s", cd['agent'])
        if cd['client']:
            query = query.filter(client=cd['client'])
            logger.info("Contracts filtered by client: %s", cd['client'])
    else:
        query = ClientContract.objects.all()
        logger.info("No filters applied to contracts.")

    query = query.order_by("-insurance_amount")
    logger.info("Contracts ordered by insurance amount.")
    return render(request, "super-contracts.html", {"contracts": query, "form": form})


def agents(request):
    if not request.user.is_superuser:
        logger.warning("Non-superuser attempted to access agents.")
        return redirect("404.html")

    form = AgentsFilterForm(request.GET or None)
    if form.is_valid():
        branch = form.cleaned_data['branch']
        if branch is None:
            agents_obj = Agent.objects.all()
        else:
            agents_obj = Agent.objects.all().filter(branch=branch)
            logger.info("Agents filtered by branch: %s", branch)
    else:
        agents_obj = Agent.objects.all()
        logger.info("No filters applied to agents.")

    return render(request, "super-agents.html", {"agents": agents_obj, "form": form})


def insurance_types(request):
    if not request.user.is_superuser:
        logger.warning("Non-superuser attempted to access insurance types.")
        return redirect("404.html")
    obj = InsuranceType.objects.all()
    logger.info("Retrieved all insurance types.")
    return render(request, "super-insurance-types.html", {"insurance_types": obj})


def stats(request):
    try:
        contracts_list = ClientContract.objects.all()
        insurance_amounts = [c.insurance_amount for c in contracts_list]
        total_sum = sum(insurance_amounts)
        mean_value = mean(insurance_amounts)
        median_value = median(insurance_amounts)
        mode_value = mode(insurance_amounts)
        logger.info("Calculated statistics: total_sum=%f, mean_value=%f, median_value=%f, mode_value=%f",
                    total_sum, mean_value, median_value, mode_value)

        reviews = Review.objects.all()
        df = pd.DataFrame(list(reviews.values_list('rating', flat=True)))
        rating_counts = df.value_counts().sort_index()

        rating_types = rating_counts.index.map(lambda m: m[0])
        rating_counts = rating_counts.values
        plt.figure(figsize=(8, 8))
        plt.pie(rating_counts, labels=rating_types, autopct='%1.1f%%', startangle=140)
        plt.title('Распределение оценок отзывов')

        image_stream = BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)
        image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

        context = {
            'total_sum': total_sum,
            'mean_value': mean_value,
            'median_value': median_value,
            'mode_value': mode_value,
            'image_base64': image_base64,
        }
        logger.info("Statistics page rendered successfully.")
    except Exception as e:
        logger.error("Error calculating statistics: %s", str(e))
        return render(request, '404.html')

    return render(request, 'super-statistics.html', context)
