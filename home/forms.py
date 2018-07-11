from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), required = False)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), required = True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required = True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), required = True)
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', )

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
