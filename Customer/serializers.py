from rest_framework import serializers
from Customer.models import Customer, Vehicle

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('ID', 'NAME', 'CARD_ID')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields=('ID','PLATE','MODEL','DESCRIPTION','CUSTOMER_ID')
        