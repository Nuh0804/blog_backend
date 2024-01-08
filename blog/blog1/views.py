#in this endpoint i created 2 endpoints with the same functionalities
#different methods one is for APIViews and the other is for Modelviewset
# I only used serializers
from .models import *
from myusers.models import User
from followers.models import *
from .serializers import *
from followers.serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

# Create your views here.
    
 #student related endpoints start here


#for viewing all student details
class StudentViewSet(ModelViewSet):
    http_method_names =['get']
    permission_classes = [IsAuthenticated]
    serializer_class = StudentRetrieveSerializer
    queryset = Student.objects.all()



#This associates this request with the current user
#create a user
class Studentagain(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        user = request.user
        student_exist = Student.objects.filter(user_id = user.id)
        serializer = StudentCreateSerializer(data=data) 
        serializer.is_valid(raise_exception=True)
        if student_exist:
            message = {'status': False, 'message':'Student exists'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user =self.request.user)
        return Response(serializer.data)
    
#student related endpoints end here


#blog endpoints start here

#getting all blogs for anyone
class BlogView(ModelViewSet):
    http_method_names = ['get']
    filter_backends = [SearchFilter]
    search_fields = ['title']
    def get_queryset(self):
        return Blog.objects.all()
    def get_serializer_class(self):
        return BlogCreateSerializer

        


#this is for student to add blog contents and view his own blogs
class myblogs(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch']

    def get_queryset(self):
        user=self.request.user
        student = Student.objects.filter(user_id = user.id)
        if student:
            blog = Blog.objects.filter(user_id = user.id)
            return blog
        message ={'status': False, 'message': 'Student not found'}
        return Student.objects.filter(user_id = user.id)

    def get_serializer_class(self):
        user=self.request.user
        student = Student.objects.filter(user_id = user.id)
        context = {'request': self.request}
        if student:
            if self.request.method == 'POST':
                return BlogCreateSerializer
            if self.request.method == 'PATCH':
                return BlogUpdateSerializer
            return userBlogSerializer
        return StudentCreateSerializer
    
    def get_serializer_context(self):
        context = {'request': self.request}
        return context
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        return Response(serializer.data)
    

#blog endpoints end here


#comment endpoint start here


class CommentView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return  comment.objects.filter(blog_id_id=self.kwargs['blog_pk'])
    def get_serializer_class(self):
        return CommentpostSerializer
    def get_serializer_context(self):
        return {'blog_id_id': self.kwargs['blog_pk']}
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        return Response (serializer.data)
    