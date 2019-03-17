from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import generic
from users.models import CustomUser
from patients.models import Profile as PatProfile
from .forms import DoctorSignUpForm


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

class DoctorDashboard(generic.ListView):
    context_object_name = 'patient_list'
    template_name = "dashboard.html"

    def get_queryset(self):
        return PatProfile.objects.filter(doctor_id=self.request.user.id).select_related()

    def get_context_data(self, **kwargs):
        context = super(DoctorDashboard, self).get_context_data(**kwargs)
        # context['star_hotels'] = Hotel.objects.all().order_by('star').reverse()[:3]
        return context


    # def get_queryset(self):
    #     user = self.request.user
    #     self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
    #     return Book.objects.filter(publisher=self.publisher)

    # def get(self, request, format=None):
    #     return Response(serializer.data)

    # def get_context_data(self, **kwargs):
    #     kwargs["user_type"] = "Doctor"
    #     return super().get_context_data(**kwargs)
