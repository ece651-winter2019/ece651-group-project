# users/urls.py
from django.urls import path
from . import views
from patients import views as patientviews
from doctors import views as doctorviews

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path(
        "signup/patient",
        patientviews.PatientSignUpView.as_view(),
        name="patient_signup",
    ),
    path("signup/doctor", doctorviews.DoctorSignUpView.as_view(), name="doctor_signup"),
]
