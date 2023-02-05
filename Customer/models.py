from django.db import models

# Create your models here.

class Vehicle(models.Model):   
    ID = models.IntegerField(primary_key=True, blank=False)
    PLATE = models.CharField(max_length=10, blank=False, default=None) 
    MODEL = models.CharField(max_length=30, blank=True)
    DESCRIPTION = models.CharField(max_length=50, blank=True)
    CUSTOMER_ID = models.ForeignKey(
    'Customer', on_delete=models.CASCADE)


class Customer(models.Model):
    ID = models.IntegerField(primary_key=True)
    NAME = models.CharField(max_length=50, blank=False)
    CARD_ID = models.CharField(max_length=10, blank=True)