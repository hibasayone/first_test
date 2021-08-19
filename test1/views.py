from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def post_blog(request):
    posts = Post.objects.all()
    for post in posts:
        post.published()
    posts = Post.objects.filter(title__contains='post')
    return render(request,'test1/post_list.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'test1/post_detail.html',{'post_detail':post})
