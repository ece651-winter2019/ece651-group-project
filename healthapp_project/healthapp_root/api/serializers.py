from rest_framework import serializers
from patients.models import PatientRecord


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = (
            "record_id",
            "patient_id",
            "bp_systolic",
            "bp_diastolic",
            "heart_rate",
            "weight",
            "created_on",
        )


class RecordsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = PatientRecord
