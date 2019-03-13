from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import generic
from users.models import CustomUser
from .forms import PatientSignUpForm


class PatientSignUpView(generic.CreateView):
    model = CustomUser
    form_class = PatientSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Patient"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user, patient_profile = form.save()
        login(self.request, user)
        return redirect("home")
