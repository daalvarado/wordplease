from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views import View
from blogs.models import BlogPost, Blog
from django.utils import timezone



class HomeView(ListView):

    model = BlogPost
    template_name = 'blogs/list.html'

    def get_queryset(self):
        result = super().get_queryset()
        return result.filter(date_posted__lt=timezone.now()).order_by('-date_created')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['claim'] = 'Check out our latest posts'
        return context


class BlogsList(ListView):

    model = Blog
    template_name = 'blogs/blogs.html'

    def get_queryset(self):
        result = super().get_queryset()
        return result.filter(blogposts__date_posted__lt=timezone.now()).order_by('blog_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blogs'
        context['claim'] = 'Check out our collection of blogs'
        return context


class UserBlogs(ListView):

    model = BlogPost
    template_name = 'blogs/list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(date_posted__lt=timezone.now()).filter(blog__author__username__iexact=self.kwargs['account']).order_by('title')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['account']+"'s Blog Posts"
        context['claim'] = 'Check out his/her collection of posts'
        return context

class PostDetail(DetailView):

    model = BlogPost
    template_name = 'blogs/post-detail.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(blog__author__username__iexact=self.kwargs['account'])


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['account'] + "'s Blog Post - ID= "+str(self.kwargs['pk'])
        context['claim'] = 'Check out this incredible post'
        return context



class MyPosts(LoginRequiredMixin, ListView):

    model = BlogPost
    template_name = 'blogs/list.html'
    login_url='/login'
    permission_denied_message = 'You must be logged in to do this!'


    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(blog__author__username__iexact=self.request.user).order_by('-date_created')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "My Posts"
        context['claim'] = 'The best blog posts in the world'
        return context

class NewPost(View):
    model = BlogPost
    template_name = 'blogs/post-detail.html'


def error_404(request):
    data = {}
    return render(request, 'blogs/404.html', data)