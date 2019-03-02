from django.db import models
from django.utils import timezone

class LoginCredentials(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=24)

class DoctorLogin(models.Model):
    login_id = models.AutoField(primary_key=True, null=False)
    doctor_id = models.ForeignKey(
        'Doctors',
        on_delete=models.CASCADE,
        null=False
        )
    created_on = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(null=False)
    
    # dont know how to add relationship for this
    # doctor = models.OneToOneField(
    #     'Doctors', 
    #     on_delete=models.CASCADE, 
    #     parent_link=True
    #     )


class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=20, null=False)
    phone_no = models.IntegerField(null=False)
    street = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=False)
    state = models.CharField(max_length=20, null=False)
    postal_code = models.CharField(max_length=6, null=False)
    country = models.CharField(max_length=20, null=False)

    # patients = [should this be foreign key in patients?]
    doc_logins = models.OneToOneField(
        DoctorLogin, 
        on_delete=models.CASCADE
        ) 



