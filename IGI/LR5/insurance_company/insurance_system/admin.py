from django.contrib import admin
from .models import *


models = (Agent, Branch, ClientContract, InsuranceObject, InsuranceType, InsuranceContract)

for m in models:
    admin.site.register(m)