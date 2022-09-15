from nis import cat
from rest_framework import serializers 
from .models import ReservableItem, ReservationItemMedia, ReservationItemData, Reservations
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User = get_user_model()

class ResItemMediaSerializer(serializers.ModelSerializer):
    class Meta: 
        model =  ReservationItemMedia
        fields = '__all__'

class ResItemSerializer(serializers.ModelSerializer):
    media = ResItemMediaSerializer(read_only=True, many=True)
    class Meta: 
        model =  ReservableItem
        fields = '__all__'

class ResSerializer(serializers.ModelSerializer):
    reservation_item = ResItemSerializer()
    class Meta: 
        model =  Reservations
        fields = '__all__'


class ResSerializerLight(serializers.ModelSerializer):
    class Meta: 
        model =  Reservations
        fields = ['start_date', 'end_date', 'reservation_item']


class ResItemDataSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ReservationItemData
        fields = '__all__'






class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.get('password')
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


        # data['password'] = make_password(password)
        print('final run--->' , data)
        return data
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ( 'email', 'password', 'password_confirmation', 'first_name', 'last_name')





# from django.contrib.auth.models import User
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.password_validation import validate_password


# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )

#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True}
#         }

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})

#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )

        
#         user.set_password(validated_data['password'])
#         user.save()

#         return user      
