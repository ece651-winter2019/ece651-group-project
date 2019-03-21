from django.urls import path
from doctors import views

urlpatterns = [
    path("", views.DoctorDashboard.as_view(), name="dashboard"),
    # path("<str:username>", views.DoctorDashboardPatientProfile.as_view(), name="patient_profile"),
    path("a", views.DoctorDashboardPatientProfile.as_view(), name="patient_profile"),
]
