from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Customer.models import Customer, Vehicle
from Customer.serializers import CustomerSerializer, VehicleSerializer


# Create your views here.

@csrf_exempt
def customerApi(request,ID=0):
    if request.method=='GET':
        customers = Customer.objects.all()
        customers_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(customers_serializer.data,safe=False)
    elif request.method=='POST':
        customer_data=JSONParser().parse(request)
        customers_serializer=CustomerSerializer(data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Adicionado", safe=False)
        return JsonResponse("Erro ao incluir", safe=False)

@csrf_exempt
def vehicleApi(request,ID=0):
    if request.method=='GET':
        vehicle = Vehicle.objects.all()
        vehicle_serializer=VehicleSerializer(vehicle,many=True)
        return JsonResponse(vehicle_serializer.data,safe=False)
    elif request.method=='POST':
        vehicle_data=JSONParser().parse(request)
        vehicle_serializer=CustomerSerializer(data=vehicle_data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return JsonResponse("Adicionado", safe=False)
        return JsonResponse("Erro ao incluir", safe=False)
    