
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories']
    search_fields = ['title', 'sub_title', 'categories']
   
admin.site.register(Post, PostAdmin)