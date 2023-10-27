# from rest_framework import serializers
# from .models import CustomUser

# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'first_name', 'last_name','password1', 'password2', 'id_number', 'phone_number','account_ammount', 'role')

from rest_framework import serializers
from .models import CustomUser

# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'first_name', 'last_name', 'id_number', 'phone_number', 'account_ammount', 'role')

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'id_number', 'phone_number', 'account_ammount', 'role')

class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('account_number','username','first_name','last_name','email','id_number','phone_number','account_ammount','role')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('account_number','username','first_name','last_name','email','id_number','phone_number','account_ammount')