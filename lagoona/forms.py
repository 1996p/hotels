from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-data username', 'placeholder': 'Login'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-data last', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-data username', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-data username', 'placeholder': 'Repeat your password'}))
    policy_agree = forms.BooleanField(label="Я согласен с условиями какой-то хуеты", widget=forms.CheckboxInput(attrs={'class': 'policy-agree'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'policy_agree')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-data username', 'placeholder': 'Login'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-data', 'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-data last', 'placeholder': 'Password'}))
