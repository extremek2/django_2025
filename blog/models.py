from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,
                            unique=True,
                            allow_unicode=True)
    def __str__(self):
        return f'{self.name} - {self.slug}'
    def get_category_url(self):
        return f'/blog/category/{self.slug}'

class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    uploaded_image = models.ImageField(upload_to='media/', blank=True, null=True)
    uploaded_file = models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return f'게시글제목: {self.title} - by {self.author} - 게시글 내용 - {self.content}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f'{self.author.username} - {self.content} in {self.post.title}'
