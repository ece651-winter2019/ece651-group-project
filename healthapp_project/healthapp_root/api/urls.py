from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # path('api/', views.api_list),
    path("api/patientrecords", views.all_patient_records.as_view()),
    path("api/patientrecords/<int:pk>/", views.patient_record.as_view()),
    path(
        "api/patientrecords/<str:username>/", views.patient_records_byusername.as_view()
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
