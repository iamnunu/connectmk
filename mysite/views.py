from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'mysite/post_list.html', {'posts': posts})


def demo(request):
    posts = Post.objects.all()
    return render(request, 'mysite/demo.html', {'posts': posts})