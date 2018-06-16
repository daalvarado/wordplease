from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Category(models.Model):
    category = models.SlugField(max_length=15, unique=True, default="Some Category")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category

    class Meta:

        verbose_name_plural = "Categories"


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogz")
    blog_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_name


class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default="", related_name="blogposts")
    owner = models.ForeignKey('auth.User', related_name='newpost', on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    summary = models.CharField(max_length=140)
    contents = models.TextField()
    image_video_url = models.FileField(upload_to='uploads', blank=True)
    categories = models.ManyToManyField(Category)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(default=timezone.now)


    objects = EntryQuerySet.as_manager()

    @property
    def publish(self):
        if self.date_posted > timezone.now():
            return 'False'
        else:
            return 'True'

    def __str__(self):
        return '{0} {1} {2}'.format(self.title, self.image_video_url, self.summary)

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-date_created"]


