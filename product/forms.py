from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

from .models import Product

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=256, min_length=4, required=True, label=_('Name'),
                                 widget=(forms.TextInput(attrs={'class': 'form-control'})))
    username = forms.EmailField(max_length=50, label=_('E-mail'),
                                widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                )
    password2 = forms.CharField(label=_('Password Confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                )

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2',)

