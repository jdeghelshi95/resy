from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ReservableItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type =  models.CharField(max_length=20, choices = [
        ['car', 'Car'],
        ['rental', 'Rental'],
        ['activity', 'Activity'],
    ])
    #(...car, activyt, rental....)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    base_price = models.FloatField()
    is_available = models.BooleanField()

class ReservationItemData(models.Model):
    key = models.CharField(max_length=20)
    value = models.TextField()
    reservation_item = models.ForeignKey(ReservableItem, on_delete=models.CASCADE)
    order = models.IntegerField()

class ReservationItemMedia(models.Model):
    reservation_item = models.ForeignKey(ReservableItem, on_delete=models.CASCADE)
    is_cover = models.BooleanField()
    file = models.FileField()
    type = models.CharField(choices=[
        ['image', 'Image'],
        ['videos', 'Video']
    ], max_length=20)
    title = models.CharField(max_length=25)
    description = models.TextField()
    order = models.IntegerField()

class Reservations(models.Model):
    reservation_item = models.ForeignKey(ReservableItem, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices = [
        ['requested', 'Requested'],
        ['rejected', 'Rejected'],
    ])
    #(...requested, rejected, booked, confiremd, completed)
    reservation_user = models.ForeignKey(User, on_delete=models.CASCADE)






























# 
# 
# 
# 
# Stay Models
# 
# 
# 
# 
# 
# 
# 
# class Stay(models.Model):
#     name = ( models.CharField(max_length = 100) )
#     guest = ( models.CharField(max_length = 100))
#     host = ( models.CharField(max_length = 100,on_delete=models.CASCADE, related_name ="Host.stay",))
#     guest_amount = ( models.IntegerField())
#     address = ( models.CharField(max_length = 200))
#     rate = ( models.CharField(max_length = 200))
#     total_price = ( models.IntegerField())
#     def __str__(self):
#         return self.name


# # Car Models

# class Car (models.Model):
#     CAR_TYPE = (
#         ('S', 'Small Sedan'),
#         ('M', 'Medium CrossOver'),
#         ('L', 'Large Suv'),

#     )
#     name = (models.CharField(max_length = 100))
#     description = (models.CharField(max_length = 300))
#     rate = (models.CharField(max_length = 50))
#     car_type = (models.CharField(max_length = 1, default= "M" , choices=CAR_TYPE))
#     total_price = (models.CharField(max_length = 50))
#     def __str__(self):
#         return self.name

# class CarRes(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.PROTECT)
#     days = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.PROTECT)


# # Activity Models

# class Activity(models.Model):
#     ACTIVITY_TYPE = (
#         ('boat', 'boat tours',),
#         ('atv', 'atv tours and rides'),
#         ('horse', 'Horse Back Riding Guided Tours'),
#         ('fish', 'guided fishing tours')
#        )
#     act_type = (models.CharField(max_length=6, choices=ACTIVITY_TYPE))
#     total_price = models.IntegerField(default=0,)
#     guest_quantity = models.IntegerField(default=1)
#     rate = models.IntegerField(default=1)
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Reservation(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
#     stay = models.ForeignKey(Stay, on_delete=models.CASCADE)
#     dateA =  models.DateField(auto_now_add=True, null=True, blank=True,)
#     dateB = models.DateField(null=True, blank=True)
#     party = models.IntegerField(null=True, blank=True)


# class Host(models.Model):
#     cars = models.ForeignKey(Car, on_delete=models.CASCADE)
#     activities = models.ForeignKey(Activity, on_delete=models.CASCADE)
#     stays = models.ForeignKey(Stay, on_delete=models.CASCADE, related_name="Stay.host")
#     user = models.ForeignKey(User, on_delete=models.CASCADE)



