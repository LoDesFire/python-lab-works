import datetime
from datetime import timezone

from django import forms

from company_info.models import PromoCode
from insurance_system.models import ClientContract, InsuranceContract, Branch, Agent
from users.models import Client


class ContractForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    insurance_amount = forms.DecimalField(widget=forms.NumberInput(attrs={'type': 'number'}))
    contract = forms.ModelChoiceField(queryset=InsuranceContract.objects.all())
    promocode = forms.CharField(max_length=10, required=False)

    class Meta:
        model = ClientContract
        fields = ("insurance_amount", "start_date", "contract")

    def clean_start_date(self):
        date = self.cleaned_data["start_date"]
        if date < datetime.datetime.now().date():
            raise forms.ValidationError("Start date cannot be in the past")

        return date

    def clean_insurance_amount(self):
        amount = self.cleaned_data["insurance_amount"]
        if amount < 0:
            raise forms.ValidationError("Insurance amount cannot be negative")

        return amount

    def clean_promocode(self):
        promocode = self.cleaned_data["promocode"]
        if promocode == "":
            return ""
        promocode_db = (PromoCode.objects.filter(to_date__gt=datetime.datetime.now().date()) & PromoCode.objects.filter(
            from_date__lte=datetime.datetime.now().date())).filter(code=promocode).first()
        if promocode_db is None:
            return forms.ValidationError("Promocode does not exist or expired")

        return promocode


class AgentsFilterForm(forms.Form):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=False)

    class Meta:
        model = None
        fields = ("branch", )


class ContractsFilterForm(forms.Form):
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=False)
    agent = forms.ModelChoiceField(queryset=Agent.objects.all(), required=False)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=False)

    class Meta:
        model = None
        fields = ("branch", "agent", "client")