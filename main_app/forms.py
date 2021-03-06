from django import forms
from .models import Link
from django.forms import ModelForm

class LinkForm(forms.ModelForm):

    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Your long URL is'}))

    class Meta:
        model = Link
        fields = ['url']