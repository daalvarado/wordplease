from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blogs.models import Blog, BlogPost
from django.contrib.auth.models import User


class BlogListSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'blog_name', 'description', 'author']


class BlogPostListSerializer(ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'image_video_url', 'summary', 'date_posted', 'owner']


class NewBlogPostSerializer(ModelSerializer):

    blog=serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all())


    class Meta:
        model = BlogPost
        fields = ['title', 'image_video_url', 'summary', 'date_posted', 'contents', 'categories', 'blog']

    def validate_blog(self, value):
        if value.author == self.context['request'].user:
            return value
        else:
            raise serializers.ValidationError('This blog does not correspond to this user')


class BlogPostDetailSerializer(ModelSerializer):

    class Meta:

        model = BlogPost
        fields = ['title', 'image_video_url', 'summary', 'date_posted', 'contents', 'categories', 'blog']

