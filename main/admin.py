from django.contrib import admin

from .models import Profile, BlogPost, BlogTag

# Register your models here.
admin.site.register(Profile)
admin.site.register(BlogPost)
admin.site.register(BlogTag)