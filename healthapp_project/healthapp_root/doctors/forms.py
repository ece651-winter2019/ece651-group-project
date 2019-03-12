from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from users.models import CustomUser
from .models import Profile


class DoctorSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )
    license_no = forms.CharField(max_length=20, required=True)
    practice_name = forms.CharField(max_length=20, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        doctor_profile = Profile(
            user_id=user,
            license_no=self.cleaned_data["license_no"],
            practice_name=self.cleaned_data["practice_name"],
        )
        doctor_profile.save()

        return user, doctor_profile
