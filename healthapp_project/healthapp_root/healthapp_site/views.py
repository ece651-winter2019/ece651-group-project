from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import generic
from users.models import CustomUser

# Function to check whether logged in user is a superuser(admin) or a regular user
# Redirect user accordingly
def home_page(request):
    if request.user.is_superuser:
        return HttpResponseRedirect("/admin/")
    else:
        return render(request, "home.html")
