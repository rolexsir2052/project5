from django import forms
from app.models import *
from django.contrib.auth.models import User
class ClientForm_User(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'