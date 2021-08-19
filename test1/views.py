from django.shortcuts import render
from .models import Post
# Create your views here.
def post_blog(request):
    posts = Post.objects.filter(title__contains='post')
    return render(request,'test1/post_list.html', {'posts': posts})