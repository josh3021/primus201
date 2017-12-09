from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Enter Username'}),
            'password' : forms.PasswordInput(attrs = {'placeholder': 'Enter Password', 'type': 'password'}),
            'email'    : forms.EmailInput(attrs = {'placeholder': 'Enter E-Mail'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
