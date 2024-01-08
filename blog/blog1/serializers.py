from django.conf import settings
from rest_framework import serializers
from .models import *
from myusers.models import *
from followers.models import *

#student serializers
class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'reg_num',
            'gender',
            'phone_num',
            'user_id',
        ]

    depth = 2


class StudentRetrieveSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField(method_name= 'count_followers')

    def count_followers(self, student:Student):
        followers = Followers.objects.filter(student = student.reg_num).count()
        return followers
    
    blog_count = serializers.SerializerMethodField(method_name='count_blogs')

    def count_blogs(self, student:Student):
        blogs = Blog.objects.filter(user_id= student.user).count()
        return blogs
    
    class Meta:
        model = Student
        fields = [
            'username',
            'reg_num',
            'phone_num',
            'gender',
            'followers',
            'blog_count'
        ]
    depth = 2

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['phone_num', 'gender']


#comment serializers
class CommentgetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = comment
        fields = [
            'user',
            'body',
            'date'
        ]
    depth = 2

class CommentpostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    def create(self, validated_data):
        blog_id = self.context['blog_id_id']
        return comment.objects.create(blog_id_id=blog_id, **validated_data)
    
    class Meta:
        model = comment
        fields = [
            'user',
            'body',
            'date'
        ]


#blog serializers
class BlogCreateSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(method_name='count_comments')
   
    def count_comments(self, blog:Blog):
        comments = comment.objects.filter(blog_id_id = blog.blog_id).count()
        return comments
  
    user = serializers.StringRelatedField()
  
    class Meta:
        model = Blog
        fields = [
            'blog_id',
            'user',
            'title',
            'description',
            'Body',
            'made',
            'comments'
        ]


class BlogUpdateSerializer(serializers.ModelSerializer):

    blog_id = serializers.ReadOnlyField()
    class Meta:
        model = Blog
        fields = [
            'blog_id',
            'title',
            'description',
            'Body'
        ]


class userBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'blog_id',
            'title',
            'description',
            'Body',
            'made'
        ]
