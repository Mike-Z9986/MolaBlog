from django.db.models.fields import EmailField
from django.shortcuts import render
from .models import Post
from marketing.models import Signup

def index(request):
    # 展现featured状态博客
    featured = Post.objects.filter(featured = True)
    # 最近三篇博客
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
        
    context = {
        'object_list' : featured,
        'latest' : latest,
    }
    return render(request, 'index.html', context)   

def blog(request):
    return render(request, 'blog.html', {}) 

def post(request):
    return render(request, 'post.html', {}) 