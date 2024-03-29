from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class":"form-control form-control-md mt-2","placeholder":"First Name"}),
            "last_name": forms.TextInput(attrs={"class":"form-control form-control-md mt-2","placeholder":"Last Name"}),
            "email": forms.EmailInput(attrs={"class":"form-control form-control-md mt-2","placeholder":"Email"}),
            "username": forms.TextInput(attrs={"class":"form-control form-control-md mt-2","placeholder":"Username"}),
            "password1": forms.PasswordInput(attrs={"class":"form-control form-control-md mt-2","placeholder":"password"}),
            "password2": forms.PasswordInput(attrs={"class":"form-control form-control-md mt-2","placeholder":"password"}),
        }


class  SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control form-control-md mt-3","placeholder":"username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-md mt-3","placeholder":"password"}))
