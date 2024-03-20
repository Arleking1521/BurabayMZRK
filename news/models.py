from django.db import models
import os
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 128)
    date = models.DateTimeField(auto_now=timezone.now)
    content = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}: {self.content} ({self.date})'
# Create your models here.

class PostAttachment(models.Model):
    file = models.FileField(upload_to='images/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)