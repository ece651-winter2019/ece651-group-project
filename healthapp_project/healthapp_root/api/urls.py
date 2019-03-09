from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.api_list),
    path('api/<int:pk>/', views.api_detail),
]