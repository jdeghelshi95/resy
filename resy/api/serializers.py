from nis import cat
from rest_framework import serializers 
from .models import ReservableItem, ReservationItemMedia, ReservationItemData, Reservations
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User = get_user_model()


class ResSerializer(serializers.ModelSerializer):
    class Meta: 
        model =  Reservations
        fields = '__all__'


class ResSerializerLight(serializers.ModelSerializer):
    class Meta: 
        model =  Reservations
        fields = ['start_date', 'end_date', 'reservation_item']

class ResItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model =  ReservableItem
        fields = '__all__'

class ResItemDataSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ReservationItemData
        fields = '__all__'

class ResItemMediaSerializer(serializers.ModelSerializer):
    class Meta: 
        model =  ReservationItemMedia
        fields = '__all__'





class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        print('password----->', password)
        password_confirmation = data.pop('password_confirmation')
        print('password con -->', password_confirmation)

        print (password != password_confirmation)
        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        print('final run--->' , data)
        return data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',)