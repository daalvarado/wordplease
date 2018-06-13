from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    slug = models.SlugField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.slug

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    summary = models.CharField(max_length=140)
    contents = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    image_video_url = models.FileField(blank=True)
    categories = models.ManyToManyField(Category, related_name='blogposts')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.title, self.image_video_url, self.summary)

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-date_created"]


