from django.db import models

# Create your models here.

class Library(models.Model):
    book_name = models.CharField(max_length=100)
    book_plot = models.TextField()
    author = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return f'책이름: {self.book_name} - 책 줄거리 - {self.book_plot}'