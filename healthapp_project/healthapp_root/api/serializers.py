from rest_framework import serializers
from patients.models import Record as PatientRecord
from users.models import CustomUser
from doctors.models import Profile as DocProfile
from patients.models import Profile as PatProfile


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = (
            "id",
            "user",
            "bp_systolic",
            "bp_diastolic",
            "heart_rate",
            "weight",
            "created_on",
            "height",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        model = CustomUser
        exclude = ("password",)


class DocProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = DocProfile
        fields = "__all__"
        extra_fields = ["user"]

    # helper function used to add extra fields on top of '__all__' fields
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(DocProfileSerializer, self).get_field_names(
            declared_fields, info
        )

        if getattr(self.Meta, "extra_fields", None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


class PatProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    doctor = DocProfileSerializer()

    class Meta:
        model = PatProfile
        fields = "__all__"
        extra_fields = ["user", "doctor"]

    # helper function used to add extra fields on top of '__all__' fields
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(PatProfileSerializer, self).get_field_names(
            declared_fields, info
        )

        if getattr(self.Meta, "extra_fields", None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
