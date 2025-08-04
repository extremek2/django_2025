from django.shortcuts import render, redirect

from .forms import PostForm, CommentForm
from .models import Post, Category, Comment


# Create your views here.

def index(request):
    # db 내에서 select * from Post 와 같은 결과
    posts_all = Post.objects.all()
    categories = Category.objects.all()
    return render(request,
                  template_name='blog/index.html',
                  context={'posts': posts_all, 'categories': categories})

def category(request, slug):
    categories = Category.objects.all()
    if slug == "no_category":
        posts = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)
    return render(request,
                  template_name='blog/index.html',
                  context={'posts': posts, 'categories': categories})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    comments = Comment.objects.filter(post=post)
    commentform = CommentForm()
    # if Comment.DoesNotExist:
    #     comments = None
    # else:
    #     comments = Comment.objects.get(pk=pk)
    return render(request,
                  template_name='blog/detail.html',
                  context={'post2': post,
                           'categories': categories,
                           'comments': comments,
                           'commentform': commentform})

def create(request):
    # form의 칸에 정보를 다 넣고 제출 버튼을 누른 경우
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

    # 'GET', 새 글 작성하기 버튼을 눌러서 create() 함수로 들어온 경우
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

# /blog/<int:pk>/delete
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/blog/')

# /blog/<int:pk>/update
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('/blog/')
    else:
        postform = PostForm(instance=post)
        return render(request,
                      template_name='blog/postupdateform.html',
                      context={'postform': postform})


def create_comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f'/blog/{post.pk}/')

def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect(f'/blog/{comment.post.pk}/')

def update_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.method == 'POST':
        commentform = CommentForm(request.POST, instance=comment)
        if commentform.is_valid():
            commentform.save()
            return redirect(f'/blog/{post.pk}/')
    else:
        commentform = CommentForm(instance=comment)
        return render(request,
                      template_name='blog/commentupdateform.html',
                      context={'commentform': commentform})


