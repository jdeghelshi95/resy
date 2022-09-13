from django.contrib import admin
from .models import ReservableItem, ReservationItemData, ReservationItemMedia, Reservations


# Register your models here.

admin.site.register(Reservations)
admin.site.register(ReservableItem)
admin.site.register(ReservationItemData)
admin.site.register(ReservationItemMedia)
