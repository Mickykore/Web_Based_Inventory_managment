from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?[0-9]+$',
        message="Phone number must contain only numeric characters or start with a plus sign."
    )
    phone = forms.CharField(validators=[phone_regex])
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password1', 'password2']
