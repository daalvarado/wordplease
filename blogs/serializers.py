from rest_framework.serializers import ModelSerializer

from blogs.models import Blog, BlogPost


class BlogListSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'blog_name', 'description', 'author']


class BlogPostListSerializer(ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'image_video_url', 'summary', 'date_posted']


class NewBlogPostSerializer(ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ['title', 'image_video_url', 'summary', 'date_posted', 'contents', 'categories', 'blog']


class BlogPostDetailSerializer(ModelSerializer):

    class Meta:

        model = BlogPost
        fields = '__all__'
