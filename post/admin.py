from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post,admin.ModelAdmin)
