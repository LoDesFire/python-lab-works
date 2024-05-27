from django.db import models
from insurance_system.models import Branch
from users.models import Client, AbstractBaseModel


class About(AbstractBaseModel):
    title = models.CharField(max_length=20)
    video_url = models.FileField(upload_to="videos/", null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    body = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return self.title


class FAQ(AbstractBaseModel):
    question = models.TextField()
    answer = models.TextField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.question


class Article(AbstractBaseModel):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.title


class PromoCode(AbstractBaseModel):
    code = models.CharField(max_length=10)
    discount = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.code + f" - ({self.discount})"


class Review(AbstractBaseModel):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.body


class Vacancy(AbstractBaseModel):
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=50)
    salary = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.position
