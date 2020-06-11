from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length = 150, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter username'
        }
    ))

    email = forms.EmailField(max_length=255, widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter email'
        }
    ))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=255)
    class Meta:
        model = User
        fields = [
            'username', 'email'
        ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image'
        ]
