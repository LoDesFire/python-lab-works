from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    username = None
    email = models.EmailField(_('Электронная почта'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Client(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"


class Employee(AbstractBaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    description = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    birth = models.DateField()

    def __str__(self):
        return self.full_name
