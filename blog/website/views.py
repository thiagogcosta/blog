from django.shortcuts import render

def hello_blog(request):
    return HttpResponse(request, 'index.html')
