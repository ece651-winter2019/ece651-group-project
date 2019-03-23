from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import generic
from users.models import CustomUser
from patients.models import Profile as PatProfile
from patients.models import Record as PatRecord
from .forms import DoctorSignUpForm
from doctors.models import Profile as DocProfile
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.contrib import messages


class DoctorSignUpView(generic.CreateView):
    model = CustomUser
    form_class = DoctorSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Doctor"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user, doctor_profile = form.save()
        login(self.request, user)
        return redirect("home")


class DoctorDashboard(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    def test_func(self):
        return self.request.user.is_doctor

    context_object_name = "patient_list"
    template_name = "dashboard.html"

    def get_queryset(self):
        """
        This will return the default query set for the class when the view method is called
        """

        return PatProfile.objects.filter(doctor_id=self.request.user.id).all()

    def get_context_data(self, **kwargs):
        """
        This will allow you to add additional fields to the context object that is sent to the view
        """
        context = super(DoctorDashboard, self).get_context_data(**kwargs)
        return context


class DoctorDashboardPatientProfile(
    LoginRequiredMixin, UserPassesTestMixin, generic.ListView
):

    # Check if doctor has permission to this specific user
    def test_func(self):
        patient_id = self.kwargs.get("userid")
        return (
            PatProfile.objects.get(user_id=patient_id).doctor_id == self.request.user.id
        )

    context_object_name = "patient_record_list"
    template_name = "patient_profile.html"

    def get_queryset(self):
        """
        This will return the default query set for the class when the view method is called
        """
        userid = self.kwargs.get("userid")
        return PatRecord.objects.filter(user_id=userid).all()

    def get_context_data(self, **kwargs):
        """
        This will allow you to add additional fields to the context object that is sent to the view
        """
        context = super(DoctorDashboardPatientProfile, self).get_context_data(**kwargs)
        return context
