from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.api_list),
    path('api/<int:pk>/', views.api_detail),
    path('api/patientrecords', views.api_list),
    path('api/patientrecords/<int:pk>/', views.api_detail),
]