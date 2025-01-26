from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'Username' }))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={ 'placeholder': 'Email' }))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={ 'placeholder': 'Password' }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={ 'placeholder': 'Password confirmation' }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLogin(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={ 'placeholder': 'Username' }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={ 'placeholder': 'Password' }))
