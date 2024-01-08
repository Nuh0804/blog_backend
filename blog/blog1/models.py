from django.db import models
from myusers.models import User
from django.conf import settings
from datetime import time, datetime

# Create your models here.

class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    reg_num = models.IntegerField(primary_key=True)
    gender_choice = [
        (MALE, 'M'),
        (FEMALE, 'F'),
    ]
    gender = models.CharField(choices=gender_choice, max_length=2)
    phone_num = models.CharField(max_length=10, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    blog_count = models.IntegerField(blank = True, null=True)
    def firstname(self):
        return self.user.first_name
    def __str__(self) -> str:
        return self.user.username
    def username(self):
        return self.user.username
    

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    Body = models.TextField()
    made = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class comment(models.Model):
    comm_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name= 'comments')
