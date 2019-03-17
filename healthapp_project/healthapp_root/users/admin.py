from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from doctors.models import Profile as DocProfile
from patients.models import Profile as PatProfile


class DocProfileInline(admin.StackedInline):
    model = DocProfile
    can_delete = False
    verbose_name_plural = "Doctor Profile"


class PatProfileInline(admin.StackedInline):
    model = PatProfile
    can_delete = False
    verbose_name_plural = "Patient Profile"


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    inlines = (DocProfileInline, PatProfileInline)

    list_display = [
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "phone_no",
        "street",
        "city",
        "state",
        "country",
        "is_doctor",
        "is_patient",
    ]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        unfiltered = super(CustomUserAdmin, self).get_inline_instances(request, obj)
        if obj.is_doctor:
            return [x for x in unfiltered if isinstance(x, DocProfileInline)]
        elif obj.is_patient:
            return [x for x in unfiltered if isinstance(x, PatProfileInline)]
        else:
            return unfiltered


actions = ["delete_selected"]


def delete_selected(self, request, obj):
    obj.delete()


admin.site.register(CustomUser, CustomUserAdmin)
