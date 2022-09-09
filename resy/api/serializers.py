from nis import cat
from rest_framework import serializers 
from .models import Car,Activity,Stay
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User = get_user_model()


class CarSerializer(serializers.ModelSerializer):
    class Meta: 
        model =  Car
        fields = '__all__'

class StaySerializer(serializers.ModelSerializer):
    class Meta: 
        model =  Stay
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta: 
        model =  Activity
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