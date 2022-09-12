from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Stay(models.Model):
    name = ( models.CharField(max_length = 100) )
    guest = ( models.CharField(max_length = 100))
    host = ( models.CharField(max_length = 100))
    guest_amount = ( models.IntegerField())
    address = ( models.CharField(max_length = 200))
    rate = ( models.CharField(max_length = 200))
    total_price = ( models.IntegerField())
    def __str__(self):
        return self.name


class Car (models.Model):
    CAR_TYPE = (
        ('S', 'Small Sedan'),
        ('M', 'Medium CrossOver'),
        ('L', 'Large Suv'),

    )
    name = (models.CharField(max_length = 100))
    description = (models.CharField(max_length = 300))
    rate = (models.CharField(max_length = 50))
    car_type = (models.CharField(max_length = 1, default= "M" , choices=CAR_TYPE))
    total_price = (models.CharField(max_length = 50))
    def __str__(self):
        return self.name

class CarRes(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    days = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Activity(models.Model):
    ACTIVITY_TYPE = (
        ('boat', 'boat tours',),
        ('atv', 'atv tours and rides'),
        ('horse', 'Horse Back Riding Guided Tours'),
        ('fish', 'guided fishing tours')
       )
    act_type = (models.CharField(max_length=6, choices=ACTIVITY_TYPE))
    total_price = models.IntegerField(default=0,)
    guest_quantity = models.IntegerField(default=1)
    rate = models.IntegerField(default=1)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



