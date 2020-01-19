
from django.contrib import admin
from .models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories']
    search_fields = ['title', 'sub_title', 'categories']
   
    
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)