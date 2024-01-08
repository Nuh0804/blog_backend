from rest_framework import serializers
from .models import *


class Followerpostserializer(serializers.ModelSerializer):
    def create(self, validated_data):
        student_pk = self.context['student']
        return Followers.objects.create(student_id=student_pk, **validated_data)
    class Meta:
        model = Followers
        fields = [

        ]


class followersgetserializer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = [
            'user',
            'student'
        ]