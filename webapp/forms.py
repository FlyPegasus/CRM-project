from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput

# Register new user

class NewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Login a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())
