from django.contrib import admin
from . import models

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['blog', 'title', 'summary', 'date_posted', 'publish']
    readonly_fields = ['publish']

admin.site.register(models.Category)
admin.site.register(models.Blog)
admin.site.register(models.BlogPost, BlogPostAdmin)



