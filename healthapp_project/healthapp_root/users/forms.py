from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.db import transaction


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    phone_no = forms.CharField(max_length=10, required=True)
    street = forms.CharField(max_length=20, required=True)
    city = forms.CharField(max_length=20, required=True)
    state = forms.CharField(max_length=2, required=True)
    postal_code = forms.CharField(max_length=6, required=True)
    country = forms.CharField(max_length=20, required=True)
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_no",
            "street",
            "city",
            "state",
            "postal_code",
            "country",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
