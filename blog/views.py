from django.shortcuts import render
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
