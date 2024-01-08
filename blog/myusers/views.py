from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,generics
from .models import User
from . serializers import *
from rest_framework import status
from rest_framework import permissions



# Create your views here.
class RegisterUserGet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'patch', 'put']
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id= user.id)
    def get_serializer_class(self):
        user = self.request.user
        user = User.objects.filter(id= user.id)
        if user:
            if self.request.method == 'GET':
                return RegisterUserSerializer
            if self.request.method == 'PATCH':
                return CurrentUserSerializer
        return RegisterUserSerializer
    
    def perform_update(self, serializer):
        serializer.save(user = self.request.user)
        return Response(serializer.data)
        

class RegisterUserPost(APIView):
    def post(self, request):
         #queryset = User.objects.get()
         serializer = RegisterUserSerializer(data= request.data)
         if serializer.is_valid():
            serializer.save()
            message = {'save': True}
            return Response(message)
         return Response(status, status= status.HTTP_400_BAD_REQUEST)


    