import logging
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from users.forms import RegisterForm, ClientRegistrationForm

logger = logging.getLogger(__name__)


def register(request):
    if request.user.is_authenticated:
        logger.info("Authenticated user tried to access the register page.")
        return redirect("index")

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        client_form = ClientRegistrationForm(request.POST)
        if form.is_valid() and client_form.is_valid():
            try:
                user = form.save(commit=False)
                client = client_form.save(commit=False)
                client.user = user
                client.email = user.email
                user.last_name = client.last_name
                user.first_name = client.first_name

                user.save()
                client.save()
                logger.info("New user registered: %s", user.email)

                return redirect('login')
            except Exception as e:
                logger.error("Error during registration: %s", str(e))
                return render(request, 'register.html', {'form': form, 'client_form': client_form, 'error': str(e)})
        else:
            logger.warning("Invalid registration form submitted.")
    else:
        form = RegisterForm()
        client_form = ClientRegistrationForm()
        logger.info("Registration page accessed.")

    return render(request, 'register.html', {'form': form, 'client_form': client_form})


def login_view(request):
    if request.user.is_authenticated:
        logger.info("Authenticated user tried to access the login page.")
        return redirect("index")

    response = requests.get('https://catfact.ninja/fact')
    fact = response.json()
    logger.info("Cat fact retrieved: %s", fact.get('fact'))

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                logger.info("User logged in: %s", email)

                next_url = request.GET.get('next')  # Get the next parameter from the URL
                if next_url:
                    logger.info("Redirecting to next URL: %s", next_url)
                    return redirect(next_url)
                else:
                    return redirect('index')
            else:
                logger.warning("Failed login attempt with email: %s", email)
        else:
            logger.warning("Invalid login form submitted.")
    else:
        form = AuthenticationForm()
        logger.info("Login page accessed.")

    return render(request, 'login.html', {'form': form, "fact": fact})


def logout_view(request):
    user_email = request.user.email if request.user.is_authenticated else "Anonymous"
    logout(request)
    logger.info("User logged out: %s", user_email)
    return redirect('login')
