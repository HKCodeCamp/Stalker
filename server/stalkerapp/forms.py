from google.appengine.ext.db import djangoforms
from stalkerapp.models import Stalker
from django import forms
from django.forms.widgets import RadioSelect
import logging

class LoginForm(djangoforms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'text'}), error_messages={'required': 'Please enter your username'})
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'text'}), error_messages={'required': 'Please enter your password'})