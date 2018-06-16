from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django.utils import timezone
from blogs.models import Blog, BlogPost
from blogs.permissions import BlogPostPermissions
from blogs.serializers import BlogListSerializer, BlogPostListSerializer, BlogPostDetailSerializer, \
    NewBlogPostSerializer
from django.db.models import Q



class BlogsViewSet(ModelViewSet):

    queryset= Blog.objects.all()
    allowed_methods = (['GET'])
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_name', 'author__first_name', 'author__last_name', 'author__username']
    ordering_fields = ['blog_name']

    def get_serializer_class(self):

        return BlogListSerializer


class BlogPostViewSet(ModelViewSet):

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return BlogPost.objects.all()
            else:
                return BlogPost.objects.filter(Q(owner=self.request.user) | Q(date_posted__lt=timezone.now()))
        else:
            return BlogPost.objects.filter(date_posted__lt=timezone.now())

    permission_classes = [BlogPostPermissions]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'contents', 'summary']
    ordering_fields = ['title', 'date_posted']
    ordering = ['-date_posted']

    def get_serializer_class(self):
        if self.action == 'create':
            return NewBlogPostSerializer
        elif self.action == 'list':
            return BlogPostListSerializer
        else:
            return BlogPostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)



class MyPostsAPI(ListAPIView):

    serializer_class = BlogPostListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BlogPost.objects.filter(blog__author__username=self.request.user)