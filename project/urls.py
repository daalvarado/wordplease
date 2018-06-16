"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    path('blogs/', include('blogs.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from blogs.api import BlogsViewSet, BlogPostViewSet, MyPostsAPI
from blogs.views import HomeView, BlogsList, UserBlogs, PostDetail, NewPost, MyPosts, NewBlog, BlogContents, MyBlogs
from accounts import views as accounts_views


router = DefaultRouter()
router.register('/blogs', BlogsViewSet)
router.register('/blogposts', BlogPostViewSet)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogs/<str:account>/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('blogs/<str:account>/<str:blogname>', BlogContents.as_view(), name='blog-contents'),
    path('blogs/<str:account>', UserBlogs.as_view(), name='user-blogs'),
    path('blogs', BlogsList.as_view(), name='blogs'),
    path('my-posts', MyPosts.as_view(), name='my-posts'),
    path('my-blogs', MyBlogs.as_view(), name='my-blogs'),
    path('new-post', NewPost.as_view(),name='new-post'),
    path('new-blog', NewBlog.as_view(),name='new-blog'),
    path('admin/', admin.site.urls),
    path('signup/', accounts_views.signup, name='acc-signup'),
    path('login', accounts_views.LoginView.as_view(), name='acc-login'),
    path('logout', accounts_views.LogoutView.as_view(), name='acc-logout'),

    #API Urls
    path('api/my-posts', MyPostsAPI.as_view(), name="api-posts-mine"),
    path('api', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

