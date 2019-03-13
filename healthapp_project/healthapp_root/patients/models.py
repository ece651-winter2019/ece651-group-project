from django.db import models
from django.utils import timezone
from django.conf import settings
from doctors.models import Profile as DocProfile


class Profile(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        parent_link=True,
        related_name="patient_profile",
    )
    doctor = models.ForeignKey(DocProfile, on_delete=models.SET_NULL, null=True)
    dob = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=10, null=False)
    contact_firstname = models.CharField(max_length=20, null=False)
    contact_lastname = models.CharField(max_length=20, null=False)
    contact_relationship = models.CharField(max_length=20, null=False)
    contact_phone = models.CharField(max_length=20, null=False)


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bp_systolic = models.IntegerField(null=False)
    bp_diastolic = models.IntegerField(null=False)
    heart_rate = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    created_on = models.IntegerField(null=False)
    height = models.CharField(max_length=6, null=False)
