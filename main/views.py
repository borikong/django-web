from django.shortcuts import render
from .models import Post


# Create your views here.

def index(request):
    postlist = Post.objects.all()
    return render(request, 'main/index.html', {'postlist': postlist})


# def blog(request):
#     postlist=Post.objects.all()
#     return render(request,'main/blog.html',{'postlist':postlist})

def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post': post})


def categorized(request, pk):
    if pk == "python-django":
        pkr = "PYTHON/DJANGO"
    elif pk == "java-spring":
        pkr = "JAVA/SPRING"
    elif pk == "android" or pk == "ml" or pk == "ps" or pk == "etc":
        pkr = pk.upper()

    postlist = Post.objects.filter(category=pkr)
    return render(request, 'main/index.html', {'postlist': postlist})
