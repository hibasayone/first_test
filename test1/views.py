from django.shortcuts import render

# Create your views here.
def post_blog(request):

    return render(request,'test1/post_list.html', {})