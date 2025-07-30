from django.shortcuts import render
from .models import Library

# Create your views here.

def index_Library(request):
    # db 내에서 select * from Library 와 같은 결과
    books_all = Library.objects.all()
    return render(request,
                  template_name='library/index.html',
                  context={'posts': books_all})

# def detail(request, pk):
#     post_detail = Post.objects.get(pk=pk)
#     return render(request,
#                   template_name='library/detail.html',
#                   context={'post2': post_detail})
