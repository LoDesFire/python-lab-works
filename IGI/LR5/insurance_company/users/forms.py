import datetime
import re
from django.contrib.auth import password_validation, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import Client


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Повтори пароль",
        required=True,
        strip=False,
        widget=forms.PasswordInput(),
    )
    email = forms.CharField(
        label="Почта",
        required=True,
    )

    class Meta:
        model = get_user_model()

        fields = ('email', "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = re.compile(
            r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
        if not pattern.match(email):
            raise forms.ValidationError("Неверно введена почта")
        return email


class ClientRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        required=True,
        label="Имя"
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        label="Фамилия"
    )
    middle_name = forms.CharField(
        max_length=50,
        required=False,
        label="Отчество"
    )
    phone_number = forms.CharField(
        max_length=50,
        required=True,
        label="Номер телефона",
    )
    address = forms.CharField(
        max_length=50,
        required=True,
        label="Адрес"
    )
    birth = forms.DateField(
        required=True,
        label="День рождения",
        widget=forms.SelectDateWidget(
            years=range(1920, (datetime.datetime.now() - datetime.timedelta(days=365 * 17)).year)),
    )

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'middle_name', 'address', 'phone_number', "birth")

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        pattern = re.compile(r"\+?375\s?\(?([0-9]{2})\)?\s?([0-9]{7})")
        match = pattern.match(phone_number)
        if not match:
            raise forms.ValidationError("Неверно введен номер телефона")

        return f"+375 ({match.group(1)}) {match.group(2)}"

    def clean_birth(self):
        birth = self.cleaned_data['birth']
        if (datetime.datetime.now().date() - birth).days < datetime.timedelta(days=365 * 18).days:
            raise forms.ValidationError("Мы работаем с клиентами от 18 лет")

        return birth
