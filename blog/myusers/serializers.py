from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = [ 'id', 'email','username', 'first_name', 'last_name']

class UserCreaterSerializer(UserCreateSerializer):
   class Meta(UserCreateSerializer.Meta):
      fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

class CurrentUserSerializer(UserSerializer):
   class Meta(UserSerializer.Meta):
      fields = ['username','first_name', 'last_name']
      