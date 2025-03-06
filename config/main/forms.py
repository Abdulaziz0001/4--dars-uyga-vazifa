from django import forms
from .models import Brand, Color

class CarsForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nomi", widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    price = forms.CharField(max_length=100, label="Narxi", widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    info = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 4
    }))
    color = forms.ModelChoiceField(queryset=Color.objects.all(), label="Rangi", widget=forms.Select(attrs={
        "class": "form-select"
    }))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), label="Brandi", widget=forms.Select(attrs={
        "class": "form-select"
    }))


