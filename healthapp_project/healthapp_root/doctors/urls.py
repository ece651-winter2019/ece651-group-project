from django.urls import path
from doctors import views

urlpatterns = [
    path("", views.DoctorDashboard.as_view(), name="dashboard"),
    # path("<str:username>", views.DoctorDashboardPatientProfile.as_view(), name="patient_profile"),
    path(
        "patient_records/<int:userid>",
        views.DoctorDashboardPatientProfile.as_view(),
        name="patient_profile",
    ),
]
