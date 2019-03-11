from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profiles(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    phone_no = models.CharField(max_length=10, null=False)
    street = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=False)
    state = models.CharField(max_length=2, null=False)
    postal_code = models.CharField(max_length=6, null=False)
    country = models.CharField(max_length=20, null=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
