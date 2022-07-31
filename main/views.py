from django.shortcuts import render
from .models import Post

## 메인페이지
def index(request):
    postlist = Post.objects.all()
    return render(request, 'main/index.html', {'postlist': postlist})


# def blog(request):
#     postlist=Post.objects.all()
#     return render(request,'main/blog.html',{'postlist':postlist})

## 상세글 보기
def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post': post})

## 카테고리별 글 정렬
def categorized(request, pk):
    pkr=None
    if pk == "python-django":
        pkr = "PYTHON/DJANGO"
    elif pk == "java-spring":
        pkr = "JAVA/SPRING"
    elif pk == "android" or pk == "ml" or pk == "ps" or pk == "etc":
        pkr = pk.upper()

    postlist = Post.objects.filter(category=pkr)
    return render(request, 'main/index.html', {'postlist': postlist})

## 새로운 글 작성 및 등록 페이지
def writing(request):
    return render(request,'main/writing.html')
## home
def home(request):
    return render(request,'main/home.html')