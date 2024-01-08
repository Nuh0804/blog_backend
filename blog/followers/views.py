from django.shortcuts import render
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class FollowersViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        student_pk = self.kwargs['students_pk']
        followers = Followers.objects.filter(student_id = student_pk, user_id = user.id)
        return followers
    def get_serializer_context(self):
        return {'student': self.kwargs['students_pk']}
    def get_serializer_class(self):
        return Followerpostserializer
    def perform_create(self, serializer):
        student_pk = self.kwargs['students_pk']
        user = self.request.user
        followers = Followers.objects.filter(student_id = student_pk, user_id = user.id)
        if followers:
            message = {'status': False, 'message': 'Already followed'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user = user)
        return Response(serializer.data)
    
