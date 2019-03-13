from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # add additional fields in here
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    phone_no = models.CharField(max_length=10, null=False)
    street = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=False)
    state = models.CharField(max_length=2, null=False)
    postal_code = models.CharField(max_length=6, null=False)
    country = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
