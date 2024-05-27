from django.contrib import admin
from .models import *

# Register your models here.
models = (About, Article, FAQ, PromoCode, Review, Vacancy)

for m in models:
    admin.site.register(m)

