from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True, null=True)
    modified_date = models.DateTimeField(auto_now=False, null=True)
    uploaded_image = models.ImageField(upload_to='media/',
                                       blank=True)

    def __str__(self):
        return f'게시글제목: {self.title} - 게시글 내용 - {self.content}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'