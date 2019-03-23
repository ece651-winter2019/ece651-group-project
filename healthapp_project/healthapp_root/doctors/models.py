from django.db import models
from django.utils import timezone
from django.conf import settings
from django import forms
from users.models import CustomUser


class Profile(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
    )
    license_no = models.CharField(max_length=20, null=False)
    practice_name = models.CharField(max_length=20, null=False)
