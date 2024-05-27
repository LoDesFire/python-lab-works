import datetime

from django.utils import timezone

from users.models import Client, AbstractBaseModel, Employee
from django.db import models


class Branch(AbstractBaseModel):
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.address


class Agent(AbstractBaseModel):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.employee.full_name}"


class InsuranceType(AbstractBaseModel):
    name = models.CharField(max_length=50)
    commission_rate = models.FloatField()

    def __str__(self):
        return self.name


class InsuranceObject(AbstractBaseModel):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(InsuranceType, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class InsuranceContract(AbstractBaseModel):
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    traffic_rate = models.FloatField()
    duration = models.DurationField(default=datetime.timedelta(hours=1))
    insurance_type = models.ForeignKey(InsuranceType, on_delete=models.SET_NULL, null=True)
    insurance_object = models.ForeignKey(InsuranceObject, on_delete=models.SET_NULL, null=True)
    clients = models.ManyToManyField(Client, through="ClientContract")

    def __str__(self):
        return f"{self.insurance_object.name}"


class ClientContract(AbstractBaseModel):
    start_date = models.DateField()
    end_date = models.DateField()
    insurance_amount = models.FloatField()
    agents_salary = models.FloatField(default=0)
    discount = models.IntegerField(null=True, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contract = models.ForeignKey(InsuranceContract, on_delete=models.CASCADE)

    def __str__(self):
        return f"ClientContract ({self.client.id} - {self.contract.id})"
