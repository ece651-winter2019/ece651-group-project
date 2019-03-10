from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Api
from api.serializers import ApiSerializer
from api.serializers import RecordsSerializer
from patients.models import PatientRecord

@csrf_exempt
def api_list(request):
    """
    List all code api's, or create a new __.
    """
    if request.method == 'GET':
        api = Api.objects.all()
        serializer = ApiSerializer(api, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ApiSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def api_detail(request, pk):
    """
    Retrieve, update or delete a code __.
    """
    try:
        api = Api.objects.get(pk=pk)
    except Api.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ApiSerializer(api)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ApiSerializer(api, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        api.delete()
        return HttpResponse(status=204)

@csrf_exempt
def all_patient_records(request):
    """
    List all patient records or add new record
    """
    if request.method == 'GET':
        record = PatientRecord.objects.all()
        serializer = RecordsSerializer(api, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecordsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def patient_record(request, pk):
    """
    Retrieve, update or delete a patient record.
    """
    try:
        record = PatientRecord.objects.get(pk=pk)
    except PatientRecord.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RecordsSerializer(record)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecordsSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        record.delete()
        return HttpResponse(status=204)
# Create your views here.
