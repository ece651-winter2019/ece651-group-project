from rest_framework import serializers
from api.models import Api, LANGUAGE_CHOICES, STYLE_CHOICES


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')