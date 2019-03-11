from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from doctors.models import Profile as DocProfile


class DocProfileInline(admin.StackedInline):
    model = DocProfile
    can_delete = False
    verbose_name_plural = "doctorprofile"


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    inlines = (DocProfileInline,)
    list_display = ["email", "username"]


admin.site.register(CustomUser, CustomUserAdmin)
