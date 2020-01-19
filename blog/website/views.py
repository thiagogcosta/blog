from django.shortcuts import render
from .models import Post, Contact

def home_blog(request):
    
    list_posts = Post.objects.all()
    
    data = {'list_posts': list_posts}
    
    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id = id)
    return render(request, 'post_detail.html', {'post': post})

def save_form(request):
    name = request.POST['name']
    Contact.objects.create(
        name = name,
        email = request.POST['email'], 
        message = request.POST['message'], 
    )
    return render(request, 'contact_succes.html', {'name_contact': name})
