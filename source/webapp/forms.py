from django import forms
from django.forms import widgets

from webapp.models import STATUS_CHOICES


class Task_form(forms.Form):
    task = forms.CharField(max_length=50, required=True, label='taskss')
    status = forms.ChoiceField( choices=STATUS_CHOICES, label='status')
    description = forms.CharField(max_length=3000, required=True, label='description')
