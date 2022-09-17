from urllib import request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import ResSerializer,ResItemSerializer, ResItemDataSerializer, UserSerializer, ResItemMediaSerializer, ResSerializerLight
from .models import ReservableItem, ReservationItemData, ReservationItemMedia, Reservations

#importing from generics?
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model, login
from django.conf import settings
from api.permissions import IsHost
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
    permission_classes = [IsHost]
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
    serializer_class = ResSerializer
    # permission_classes = (IsAuthenticated,)
    
    queryset = Reservations.objects.all()
    def get_queryset(self):
        return Reservations.objects.filter(reservation_user=self.request.user)

    def perform_create(self, serializer):
        save_data = {}
        save_data["start_date"]  = self.request.data.get('start_date', "")
        save_data["end_date"]  = self.request.data.get('end_date', "")
        save_data["reservation_user"]  = self.request.data.get('reservation_user', 0)

        reservation_item = self.request.data.get('reservation_item', 0)
        reservation = ReservableItem.objects.get(pk=reservation_item)

        save_data["reservation_item"] = reservation
        
        serializer.save(**save_data)



    #   class ReservationView(APIView):
    # def get(self, request):
    #     reservation = Reservations.objects.all()
    #     serializer = ResSerializer(reservation, many=True)
    #     return Response(serializer.data)


# Reservation Media --------------------------------------------------------------

class ReservationMediaView(viewsets.ModelViewSet):
    serializer_class = ResItemMediaSerializer
    #queryset = ReservationItemMedia.objects.all()

    def get_queryset(self):
        qs = ReservationItemMedia.objects.all()
        r = self.request.GET.get('reservation')
        if r:
            qs = qs.filter(reservation_item_id=r)
        return qs

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



# test user ------------------------------
# {"email":"apple@gmail.com", "password":"Helloworld123"}

# # USER AUTHENTICATION ----------------------------------------------------------------
# class LoginView(APIView):
#     def get_user(self, email):
#         try: 
#             return User.objects.get(email=email)
#             # return User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise PermissionDenied({'message': 'Invalid Credentials'})

#     def post(self, request):

#         email = request.data.get('email')
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = self.get_user(email)
#         # user = self.get_user(username)
#         if not user.check_password(password):
#             raise PermissionDenied({'message': 'Invalid Credentials'})
        
#         token = jwt.encode({'sub': user.id}, settings.SECRET_KEY, algorithm='HS256')
#         login(self.request, user)
#         return Response({'token': token, 'message': f'Welcome back {user.username}!'})

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration Successful!!!'})
        return Response(serializer.errors, status=422)


class LoginView(ObtainAuthToken):
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'id': user.id,
            'token': token.key
        })

class HealthCheckView(APIView):
     def get(self, request):
           return Response({"status": True})


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




