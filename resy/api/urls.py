from django.urls import path
from . import views

urlpatterns = [
# Cars
path('cars-list/', views.CarsView.as_view(), name="cars-list"),
path('cars-list/<int:pk>/', views.CarDetail.as_view(), name="cars"),
path('cars-res-list/', views.CarResView.as_view(), name="cars-res"),
# stays
path('stays-list/', views.StaysView.as_view(), name="stays-list"),
path('activities-list/', views.ActivitiesView.as_view() , name="activities-list"),
path('register/', views.RegisterView.as_view() , name="register"),
path('login/', views.LoginView.as_view() , name="login"),
]