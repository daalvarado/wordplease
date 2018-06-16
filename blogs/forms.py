from django.core.exceptions import ValidationError
from django.forms import ModelForm

from blogs.models import Blog, BlogPost



class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author']

    def clean(self):
        super().clean()

class BlogPostForm(ModelForm):



    class Meta:
        model = BlogPost
        fields = '__all__'
        exclude = ['owner']



    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(author__username=request.user)

    def clean_image(self):
        image_video_url = self.cleaned_data.get('image_video_url')
        if image_video_url is not None and 'image' not in image_video_url.content_type:
            raise ValidationError('The file is not a valid type')
        return image_video_url

    def clean(self):
        super().clean()
