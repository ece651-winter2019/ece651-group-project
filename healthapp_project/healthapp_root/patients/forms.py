from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from .models import Profile


class PatientSignUpForm(UserCreationForm):
    # interests = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )
    doctor_id = forms.IntegerField(required=True)
    dob = forms.CharField(max_length=10, required=True)
    sex = forms.CharField(max_length=10, required=True)
    contact_firstname = forms.CharField(max_length=20, required=True)
    contact_lastname = forms.CharField(max_length=20, required=True)
    contact_relationship = forms.CharField(max_length=20, required=True)
    contact_phone = forms.CharField(max_length=20, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient_profile = Profile(
            user_id=user,
            doctor_id=self.cleaned_data["doctor_id"],
            dob=self.cleaned_data["dob"],
            sex=self.cleaned_data["sex"],
            contact_firstname=self.cleaned_data["contact_firstname"],
            contact_lastname=self.cleaned_data["contact_lastname"],
            contact_relationship=self.cleaned_data["contact_relationship"],
            contact_phone=self.cleaned_data["contact_phone"],
        )
        patient_profile.save()

        return user, patient_profile
