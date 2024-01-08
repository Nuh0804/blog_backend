from django.db import models
from blog1.models import *
from django.conf import settings
# Create your models here.

class Followers(models.Model):
    student = models.ForeignKey(Student, related_name='followers', on_delete= models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
