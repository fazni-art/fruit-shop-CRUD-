from django import forms
from .models import frutables


class NewForm(forms.ModelForm):
    class Meta:
        model=frutables
        fields=['name','desc','price','image']