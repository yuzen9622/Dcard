from django.contrib import admin
from .models import Post,Comment
# Register your models here.
admin.site.register(Post,admin.ModelAdmin)
admin.site.register(Comment,admin.ModelAdmin)