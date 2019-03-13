from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from doctors.models import Profile as DocProfile
from patients.models import Profile as PatProfile


# class DocProfileInline(admin.StackedInline):
#     model = DocProfile
#     can_delete = False
#     verbose_name_plural = "doctor profile"


# class PatProfileInline(admin.StackedInline):
#     model = PatProfile
#     can_delete = False
#     verbose_name_plural = "patient profile"


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # inlines = (DocProfileInline, PatProfileInline)
    list_display = ["id", "email", "username", "first_name", "last_name"]


admin.site.register(CustomUser, CustomUserAdmin)
