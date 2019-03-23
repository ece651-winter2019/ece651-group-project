# django imports
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

# rest framework imports
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# import rest framework and django filters
import rest_framework_filters as filters
import django_filters

# import serializers
from api.serializers import RecordsSerializer
from api.serializers import UserSerializer, PatProfileSerializer, DocProfileSerializer

# import api permissions
from api.permissions import IsPatientUser

# Import models
from patients.models import Record as PatientRecord
from patients.models import Profile as PatProfile
from doctors.models import Profile as DocProfile
from users.models import CustomUser


class DateTimeFilter(filters.FilterSet):
    created_date = filters.DateTimeFilter(field_name="created_on")

    class Meta:
        model = PatientRecord
        fields = {"created_on": ["gte", "lte", "gt", "lt"]}


class all_patient_records(ListAPIView):
    # Allow for requests only if user is authenticated
    permission_classes = (IsAuthenticated, IsPatientUser)
    serializer_class = RecordsSerializer

    # Added filters to this view
    ordering_fields = "created_on"
    filter_class = DateTimeFilter
    queryset = PatientRecord.objects.all()

    """
    List all patient records or add new record
    """

    def post(self, request, format=None):
        userid = request.user.id
        data = request.data
        if type(request.data) == list:
            for d in data:
                d["user"] = userid
            serializer = RecordsSerializer(data=data, many=True)
        else:
            data["user"] = userid
            serializer = RecordsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class patient_record(APIView):

    # Allow for requests only if user is authenticated
    permission_classes = (IsAuthenticated, IsPatientUser)
    """
    Retrieve, update or delete a record instance.
    """

    def get_object(self, pk):
        try:
            return PatientRecord.objects.get(pk=pk)
        except PatientRecord.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = RecordsSerializer(record)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        record = self.get_object(pk)
        serializer = RecordsSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        record = self.get_object(pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class patient_records_byusername(APIView):

    # Allow for requests only if user is authenticated
    permission_classes = (IsAuthenticated, IsAdminUser)
    """
    Retrieve, update or delete a record instance.
    """

    def get_object(self, username):
        try:
            userid = CustomUser.objects.get(username=username).id

            return PatientRecord.objects.filter(user_id=userid).all()
        except CustomUser.DoesNotExist:
            raise Http404
        except PatientRecord.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        record = self.get_object(username)
        serializer = RecordsSerializer(record, many=True)
        return Response(serializer.data)

    def post(self, request, username, format=None):
        if type(request.data) == list:
            userid = CustomUser.objects.get(username=username).id
            data = request.data
            for d in data:
                d["user"] = userid
            serializer = RecordsSerializer(data=data, many=True)
        else:
            userid = CustomUser.objects.get(username=username).id
            data = request.data
            data["user"] = userid
            serializer = RecordsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, username, format=None):
        record = self.get_object(username)
        serializer = RecordsSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        record = self.get_object(username)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Users(ListAPIView):
    # Allow for requests only if user is authenticated
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class Patients(ListAPIView):
    # Allow for requests only if user is authenticated
    queryset = PatProfile.objects.all()
    serializer_class = PatProfileSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class Doctors(ListAPIView):
    # Allow for requests only if user is authenticated
    queryset = DocProfile.objects.all()
    serializer_class = DocProfileSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)
