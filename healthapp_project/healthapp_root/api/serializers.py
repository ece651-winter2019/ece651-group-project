from rest_framework import serializers
from api.models import Api, LANGUAGE_CHOICES, STYLE_CHOICES
from patients.models import PatientRecord

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = ('record_id', 'patient_id', 'bp_systolic', 'bp_diastolic', 'heart_rate', 'weight', 'created_on')

    