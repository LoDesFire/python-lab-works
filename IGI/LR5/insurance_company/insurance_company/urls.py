"""
URL configuration for insurance_company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from users import views as user
from insurance_system import views as system
from company_info import views as info

urlpatterns = [
    path('register/', user.register, name='register'),
    path('login/', user.login_view, name='login'),
    path('logout/', user.logout_view, name='logout'),

    path('profile/', system.profile, name='profile'),

    path('', info.about, name='index'),
    path('contacts/', info.contacts, name='contacts'),
    path('faq/', info.faq, name='faq'),
    path('news/', info.news, name='news'),
    path('reviews/', info.reviews, name='reviews'),
    path("reviews/create/", info.create_review, name="create-review"),
    path("promos/", info.promocodes, name="promos"),
    path("contract/new/", system.new_contract, name="new-contract"),

    path("contracts/", system.view_contracts, name="agent-contracts"),
    path("admin/", admin.site.urls),
    path("superuser/filials/", system.filials, name="filials-list"),
    path("superuser/contracts/", system.contracts, name="contracts-list"),
    path("superuser/agents/", system.agents, name="agents-list"),
    path("superuser/insurance_types/", system.insurance_types, name="insurance-types"),
    path("superuser/stats", system.stats, name="statistics")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
