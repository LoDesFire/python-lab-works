import logging

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from company_info.forms import ReviewForm
from company_info.models import Article, FAQ, Review, About, PromoCode, Vacancy
from users.models import Employee

logger = logging.getLogger(__name__)


def about(request):
    try:
        about_obj = About.objects.first()
        article = Article.objects.order_by('-created_at').first()
        logger.info("About page accessed.")
        return render(request, 'index.html', {'article': article, "about": about_obj})
    except Exception as e:
        logger.error("Error accessing about page: %s", str(e))
        return render(request, '404.html')


def news(request):
    try:
        articles = Article.objects.all().order_by('-created_at')
        logger.info("News page accessed. Number of articles: %d", len(articles))
        return render(request, 'news.html', {'articles': articles})
    except Exception as e:
        logger.error("Error accessing news page: %s", str(e))
        return render(request, '404.html')


def faq(request):
    try:
        faqs = FAQ.objects.all().order_by('-created_at')
        logger.info("FAQ page accessed. Number of FAQs: %d", len(faqs))
        return render(request, 'faq.html', {"faqs": faqs})
    except Exception as e:
        logger.error("Error accessing FAQ page: %s", str(e))
        return render(request, '404.html')


def contacts(request):
    try:
        employees = Employee.objects.all()
        vacancies = Vacancy.objects.all()
        logger.info("Contacts page accessed. Number of employees: %d, number of vacancies: %d", len(employees),
                    len(vacancies))
        return render(request, 'contacts.html', {"employees": employees, "vacancies": vacancies})
    except Exception as e:
        logger.error("Error accessing contacts page: %s", str(e))
        return render(request, '404.html')


def reviews(request):
    try:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        joke = response.json()
        reviews_list = Review.objects.all().order_by('-created_at')
        logger.info("Reviews page accessed. Number of reviews: %d", len(reviews_list))
        return render(request, 'reviews.html', {'reviews': reviews_list, 'joke': joke})
    except Exception as e:
        logger.error("Error accessing reviews page: %s", str(e))
        return render(request, '404.html')


@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                review = form.save(commit=False)
                review.client = request.user.client
                review.save()
                logger.info("New review created by client: %s", review.client)
                return redirect("index")
            except Exception as e:
                logger.error("Error creating review: %s", str(e))
        else:
            logger.warning("Invalid review form submitted.")
    else:
        logger.info("Create review page accessed.")
        review_form = ReviewForm()
    return render(request, 'create_review.html', {'form': review_form})


@login_required
def promocodes(request):
    try:
        active_promo = (PromoCode.objects.filter(from_date__lte=timezone.now()) & PromoCode.objects.filter(
            to_date__gte=timezone.now())).all().order_by('-from_date')
        archive_promo = PromoCode.objects.filter(to_date__lt=timezone.now()).all().order_by('-from_date')
        logger.info("Promocodes page accessed. Active promocodes: %d, Archived promocodes: %d", len(active_promo),
                    len(archive_promo))
        return render(request, "promos.html", {"active_promo": active_promo, "archive_promo": archive_promo})
    except Exception as e:
        logger.error("Error accessing promocodes page: %s", str(e))
        return render(request, '404.html')
