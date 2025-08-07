from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PostForm, CommentForm
from .models import Post, Category, Comment


# CBV 방식 view 정의

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    # template_name = post_confirm_delete.html

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category', 'uploaded_image','uploaded_file']

# /blog/pk
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

# post_form.html
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'uploaded_image','uploaded_file']
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreateView, self).form_valid(form)
        else:
            return redirect('/blog/')
# template_name = '/blog/post_list.html
# context -> post들 -> post_list
# 모델명에 따라서 대문자->소문자_list
# Comment --> comment_list
class PostListView(ListView):
    model = Post
    ordering = ['-pk']



# FBV 방식 view 정의

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

@login_required(login_url='/accounts/google/login/')
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
                  context={'post': post,
                           'categories': categories,
                           'comments': comments,
                           'commentform': commentform})

@login_required(login_url='/accounts/google/login/')
def create(request):
    # form의 칸에 정보를 다 넣고 제출 버튼을 누른 경우
    # 작성 하다가 제출 버튼을 누른 경우
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        # 정상 값인 경우
        if postform.is_valid():
            post1 = postform.save(commit=False)
            post1.author = request.user
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

@login_required(login_url='/accounts/google/login/')
# /blog/<int:pk>/delete
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/blog/')

@login_required(login_url='/accounts/google/login/')
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

@login_required(login_url='/accounts/google/login/')
def create_comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(f'/blog/{post.pk}/')

@login_required(login_url='/accounts/google/login/')
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect(f'/blog/{comment.post.pk}/')

@login_required(login_url='/accounts/google/login/')
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


