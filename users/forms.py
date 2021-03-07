from django.forms import forms

from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'last_name', 'email', 'password1', 'password2')
