from django import forms
from django.contrib.auth.models import User # built-in model
from django.contrib.auth.forms import UserCreationForm # has only 3 built-in fields (username, password1 and password2)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']