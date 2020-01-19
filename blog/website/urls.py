
from django.urls import path
from .views import home_blog
from .views import post_detail

urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),
]
