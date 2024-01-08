from django.urls import path
from . import views
from followers.views import FollowersViewset
from rest_framework_nested import routers
# from rest_framework import routers#

router =routers.DefaultRouter()
router.register('students', viewset=views.StudentViewSet, basename='students')# see all student details
router.register('blogs', viewset=views.BlogView, basename='blogs') # all blogs get method for anynone
router.register('userblogs', viewset=views.myblogs, basename='userblogs') #blogs for specific user to add and edit

followers_router = routers.NestedDefaultRouter(router, 'students', lookup = 'students')
followers_router.register('followers', viewset=FollowersViewset, basename='followers')

comments_router = routers.NestedDefaultRouter(router, 'blogs', lookup = 'blog')
comments_router.register('comments', views.CommentView, basename= 'blog-comments')

urlpatterns = [
    path('student create/', views.Studentagain.as_view()), # create a student
]+ router.urls+ comments_router.urls + followers_router.urls
   
   