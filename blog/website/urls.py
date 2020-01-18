
from django.urls import path, include
from .vews import hello_blog

urlpatterns = [
    path('', hello_blog),

]
