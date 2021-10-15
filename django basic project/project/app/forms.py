from django import forms
from django.forms import ModelForm
from .models import webdata


class frontform(ModelForm):
    class Meta:
        model = webdata
        fields={'name','age','comment'}
