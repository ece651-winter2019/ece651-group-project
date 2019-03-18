from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("users", views.Users.as_view()),
    path("patients", views.Patients.as_view()),
    path("doctors", views.Doctors.as_view()),
    path("patientrecords", views.all_patient_records.as_view()),
    path("patientrecords/<int:pk>", views.patient_record.as_view()),
    path("patientrecords/<str:username>", views.patient_records_byusername.as_view()),
    path("token-auth", obtain_auth_token, name="api_token_auth"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
