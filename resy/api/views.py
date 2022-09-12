from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import CarSerializer,StaySerializer, ActivitySerializer, UserSerializer, CarResSerializer
from .models import Car,Stay,Activity,CarRes
#importing from generics?
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
User = get_user_model()



# Create your views here.
# Car Views
class CarsView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
# class CarCreate
class CarDetail(APIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarResView(APIView):
    def get(self, request):
        cars = CarRes.objects.all()
        serializer = CarResSerializer(cars, many=True)
        return Response(serializer.data)




# Stay Views
class StaysView(APIView):
    def post(self, request):
        stays = Stay.objects.all()
        serializer = StaySerializer(stays, many=True)
        return Response(serializer.data)

# Actviity Views
class ActivitiesView(APIView):
    def post(self, request):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful!!!'})
        return Response(serializer.errors, status=422)


class LoginView(APIView):
    def get_user(self, email):
        try: 
            return User.objects.get(email=email)
            # return User.objects.get(username=username)
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Invalid Credentials'})

    def post(self, request):

        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')

        user = self.get_user(email)
        # user = self.get_user(username)
        if not user.check_password(password):
            raise PermissionDenied({'message': 'Invalid Credentials'})
        
        token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')

        return Response({'token': token, 'message': f'Welcome back {user.username}!'})


