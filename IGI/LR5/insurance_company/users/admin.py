from django.contrib import admin
from .models import User, Client, Employee

models = (User, Client, Employee)

for m in models:
    admin.site.register(m)
