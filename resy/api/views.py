from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import ResSerializer,ResItemSerializer, ResItemDataSerializer, UserSerializer, ResItemMediaSerializer
from .models import ReservableItem, ReservationItemData, ReservationItemMedia, Reservations

#importing from generics?
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
User = get_user_model()

# Create your views here.


# Reservation Item Views================================================================
# class ResItemView(APIView):
#     def get(self, request):
#         res_item = ReservableItem.objects.all()
#         serializer = ResItemSerializer(res_item, many=True)
#         return Response(serializer.data)

class ResItemView(viewsets.ModelViewSet):
    serializer_class = ResItemSerializer
    #queryset = ReservableItem.objects.all()

    def get_queryset(self):
        qs = ReservableItem.objects.all()
        t = self.request.GET.get('type')
        if t:
            qs = qs.filter(type=t)
        return qs

# class ResDetail(self, res_item_id):

#     resitem = ReservableItem.objects.get(id=res_item_id)
#     return Response()


# Reservation View ----------------------------------------------------------------

class ReservationView(viewsets.ModelViewSet):
    serializer_class= ResSerializer
    queryset = Reservations.objects.all()


    #   class ReservationView(APIView):
    # def get(self, request):
    #     reservation = Reservations.objects.all()
    #     serializer = ResSerializer(reservation, many=True)
    #     return Response(serializer.data)


# Reservation Media --------------------------------------------------------------

class ReservationMediaView(viewsets.ModelViewSet):
    serializer_class = ResItemMediaSerializer
    queryset = ReservationItemMedia.objects.all()


# class ReservationMediaView(APIView):
#     def get(self, request):
#         res_media = ReservationItemMedia.objects.all()
#         serializer = ResItemMediaSerializer(res_media, many=True)
#         return Response(serializer.data)




# RESERVATION ITEM DATA ------------------------------------------------------------------------------------
class ReservationDataView(viewsets.ModelViewSet):
    serializer_class= ResItemDataSerializer
    queryset = ReservationItemData.objects.all()

# class ReservationDataView(APIView):
#     def get(self, request):
#         res_data = ReservationItemData.objects.all()
#         serializer = ResItemDataSerializer(res_data , many=True)
#         return Response(serializer.data)



# USER AUTHENTICATION ----------------------------------------------------------------
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

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful!!!'})
        return Response(serializer.errors, status=422)







# # class CarCreate
# class CarDetail(APIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer

# class CarResView(APIView):
#     def get(self, request):
#         cars = CarRes.objects.all()
#         serializer = CarResSerializer(cars, many=True)
#         return Response(serializer.data)




# # Stay Views
# class StaysView(APIView):
#     def post(self, request):
#         stays = Stay.objects.all()
#         serializer = StaySerializer(stays, many=True)
#         return Response(serializer.data)

# # Actviity Views
# class ActivitiesView(APIView):
#     def post(self, request):
#         activities = Activity.objects.all()
#         serializer = ActivitySerializer(activities, many=True)
#         return Response(serializer.data)




