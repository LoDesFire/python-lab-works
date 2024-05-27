from django import forms
from django.utils.safestring import mark_safe

from company_info.models import Review
from insurance_company import settings


class ReviewForm(forms.ModelForm):
    body = forms.TextInput()
    rating = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class": "horizontal-radio"}), choices={k: k for k in range(1, 6)})

    class Meta:
        model = Review
        fields = ("body", "rating")
