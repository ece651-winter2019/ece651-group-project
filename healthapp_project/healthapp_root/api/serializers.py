from rest_framework import serializers
from patients.models import Record as PatientRecord


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


class RecordsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = PatientRecord
