from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return f'게시글제목: {self.title} - 게시글 내용 - {self.content}'