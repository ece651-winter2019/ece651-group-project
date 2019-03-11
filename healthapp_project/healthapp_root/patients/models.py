from django.db import models
from django.utils import timezone


# class PatientLogin(models.Model):
#     # patient = models.OneToOneField(
#     #     'Patients',
#     #     on_delete = models.CASCADE,
#     # )
#     login_id = models.AutoField(primary_key=True)
#     patient_id = models.OneToOneField("Patients", on_delete=models.CASCADE, null=False)
#     created_on = models.DateTimeField(default=timezone.now)
#     status = models.IntegerField(null=False)


# class Patients(models.Model):
#     patient_id = models.AutoField(primary_key=True)
#     doctor_id = models.ForeignKey(
#         "doctors.doctors", on_delete=models.CASCADE, null=False
#     )
#     first_name = models.CharField(max_length=20, null=False)
#     last_name = models.CharField(max_length=20, null=False)
#     dob = models.CharField(max_length=10, null=False)
#     sex = models.CharField(max_length=10, null=False)
#     height = models.CharField(max_length=6, null=False)
#     email = models.CharField(max_length=20, null=False)
#     phone_no = models.CharField(max_length=20, null=False)
#     street = models.CharField(max_length=20, null=False)
#     city = models.CharField(max_length=20, null=False)
#     state = models.CharField(max_length=2, null=False)
#     postal_code = models.CharField(max_length=6, null=False)
#     country = models.CharField(max_length=20, null=False)
#     emergency_C = models.OneToOneField("EmergencyContacts", on_delete=models.CASCADE)
#     # don't need this
#     # doctor = models.ForeignKey('doctors.doctors')
#     health_stats = models.OneToOneField("HealthStats", on_delete=models.CASCADE)
#     # logins =


# class HealthStats(models.Model):
#     record_id = models.AutoField(primary_key=True)
#     patient_id = models.OneToOneField(Patients, on_delete=models.CASCADE)
#     bp_systolic = models.IntegerField(null=False)
#     bp_diastolic = models.IntegerField(null=False)
#     heart_rate = models.IntegerField(null=False)
#     weight = models.IntegerField(null=False)
#     updated = models.DateTimeField(default=timezone.now)


# class EmergencyContacts(models.Model):
#     patient_id = models.OneToOneField(Patients, on_delete=models.CASCADE)
#     contact_firstname = models.CharField(max_length=20, null=False)
#     contact_lastname = models.CharField(max_length=20, null=False)
#     relationship = models.CharField(max_length=20, null=False)
#     phone = models.CharField(max_length=20, null=False)


class PatientRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    # patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    patient_id = models.IntegerField(null=False)
    bp_systolic = models.IntegerField(null=False)
    bp_diastolic = models.IntegerField(null=False)
    heart_rate = models.IntegerField(null=False)
    weight = models.IntegerField(null=False)
    created_on = models.IntegerField(null=False)
