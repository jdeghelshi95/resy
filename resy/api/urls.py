from django.urls import path
from . import views

urlpatterns = [
path('cars-list/', views.CarsView.as_view(), name="cars-list"),
path('stays-list/', views.StaysView.as_view(), name="stays-list"),
path('activities-list/', views.ActivitiesView.as_view() , name="activities-list"),
path('register/', views.RegisterView.as_view() , name="register"),
path('login/', views.LoginView.as_view() , name="login"),
]sadfasdfaa