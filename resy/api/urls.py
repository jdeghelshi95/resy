from django.urls import path
from rest_framework import routers
from . import views



# urlpatterns = [
# path('register/', views.RegisterView.as_view() , name="register"),
# path('login/', views.LoginView.as_view() , name="login"),


# ]

router = routers.SimpleRouter()
router.register(r'reservable-items', views.ResItemView)
router.register(r'reservations', views.ReservationView)
router.register(r'res-media', views.ReservationMediaView)
router.register(r'res-data', views.ReservationDataView)

urlpatterns = router.urls



# # reservation items
# path('res-items/', views.ResItemView.as_view(), name="res-items"),
# # path('res-items/<int:pk>/', views.ResItemDetail , name="res-item-details"),
# # reservations
# path('res/', views.ReservationView.as_view(), name="reservations-view"),

# # reservation data
# path('res-data/', views.ReservationDataView.as_view(), name="res-data-view"),

# # reservation media
# path('res-media/', views.ReservationMediaView.as_view(), name="res-media-view"),
# path('cars-list/<int:pk>/', views.CarDetail.as_view(), name="cars"),
# path('cars-res-list/', views.CarResView.as_view(), name="cars-res"),
# stays
# path('stays-list/', views.StaysView.as_view(), name="stays-list"),
# path('activities-list/', views.ActivitiesView.as_view() , name="activities-list"),
