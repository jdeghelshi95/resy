from django.db import models

# Create your models here.

class Stays(models.Model):
    guest = ( models.CharField(max_length = 100))
    host = ( models.CharField(max_length = 100))
    guest_amount = ( models.IntegerField())
    address = ( models.CharField(max_length = 200))
    price = ( models.CharField(max_length = 200))

    def __str__(self):
        return self.name


class Cars (models.Model):
    CAR_TYPE = (
        ('S', 'Small Sedan'),
        ('M', 'Medium CrossOver'),
        ('L', 'Large Suv'),
    )
    name = (models.CharField(max_length = 100))
    description = (models.CharField(max_length = 300))
    fee = (models.CharField(max_length = 50))

    def __str__(self):
        return self.name