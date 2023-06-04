from django import forms
from .models import Creator

class CreatorsForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'
