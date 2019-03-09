from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Api
from api.serializers import ApiSerializer

@csrf_exempt
def api_list(request):
    """
    List all code api's, or create a new api.
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
    Retrieve, update or delete a code api.
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
# Create your views here.
