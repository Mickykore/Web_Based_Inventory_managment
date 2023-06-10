from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='ET')
    )
    class Meta:
        model = Profile
        fields = ['phone', 'image']
        
class PhoneForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='ET')
    )
    class Meta:
        model = Profile
        fields = ['phone']