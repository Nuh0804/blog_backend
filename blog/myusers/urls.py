
from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.RegisterUserGet, basename='user')
urlpatterns = [
    # path('', views.RegisterUserGet.as_view({'get': 'list'}), name= 'registeruser'),
     path('register', views.RegisterUserPost.as_view(), name= 'registeruser')
] + router.urls