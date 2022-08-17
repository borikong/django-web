from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm,DeleteForm

## 메인페이지
def index(request):
    postlist = Post.objects.all()
    return render(request, 'main/index.html', {'postlist': postlist})

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
    elif pk == "android" or pk == "ml" or pk == "ps" or pk=="guest" or pk == "etc":
        pkr = pk.upper()

    postlist = Post.objects.filter(category=pkr)
    return render(request, 'main/index.html', {'postlist': postlist})

## 새로운 글 작성 및 등록 페이지
def writing(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            # user_id=request.session.get('user')
            post=Post()
            post.category='GUEST'
            post.user=form.cleaned_data['name']
            post.postname=form.cleaned_data['postname']
            post.contents=form.cleaned_data['contents']
            post.passwd = form.cleaned_data['passwd']
            post.save()
            return redirect('/')
    else:
        form=PostForm()
    return render(request,'main/writing.html',{'form':form })

##글 삭제
def delete(request,pk):
    post = Post.objects.get(pk=pk)
    upasswd = request.POST.get("passwd")
    # print("유저패스워드", upasswd)

    if request.method=="POST":
        upasswd = request.POST.get("passwd")
        print("유저패스워드", upasswd)
        if upasswd==post.passwd:
            post.delete()
            return redirect('/')
        else:
            print('비밀번호 오류1')
    else:
        print('비밀번호 오류2')

    return redirect('/')

## home
def home(request):
    return render(request,'main/home.html')