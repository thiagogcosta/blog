
from django.urls import path
from .views import home_blog
from .views import post_detail, save_form

urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('save_form', save_form, name='save_form'),
]
