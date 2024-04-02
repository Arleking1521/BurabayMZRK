from django.db import models
from django.utils import timezone

class Reviews(models.Model):
    author = models.CharField(verbose_name = "ФИО")
    IIN = models.CharField(verbose_name = 'ИИН')
    review = models.TextField(verbose_name='Отзыв')
    date = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return f'{self.author}: {self.IIN} ({self.date})'
    
class Answer(models.Model):
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='Ответ на отзыв')
    date = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return f'{self.review.author}: {self.answer} ({self.date})'