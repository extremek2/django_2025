from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post

# Create your views here.

def index(request):
    # db 내에서 select * from Post 와 같은 결과
    posts_all = Post.objects.all()
    return render(request,
                  template_name='blog/index.html',
                  context={'posts': posts_all})

def detail(request, pk):
    post_detail = Post.objects.get(pk=pk)
    return render(request,
                  template_name='blog/detail.html',
                  context={'post2': post_detail})

def create(request):
    # 작성 하다가 제출 버튼을 누른 경우
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        # 정상 값인 경우
        if postform.is_valid():
            post1 = postform.save(commit=False)
            post1.title += "홍길동 만세"
            post1.save()
            return redirect('/blog/')
        # 비정상인 경우

    # 'GET'
    else:
        postform = PostForm()
        return render(request,
                      template_name='blog/postform.html',
                      context={'postform': postform})

def create_fake(request):
    post = Post()
    post.title = "새싹 용산구"
    post.content = "나진상가 3층"
    post.save()
    return redirect('/blog/')