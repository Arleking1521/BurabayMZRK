from django.utils import timezone
from django.db import models

# Create your models here.
class Ads(models.Model):
    title = models.CharField(verbose_name = 'Заголовок объявления')
    
    def __str__(self) -> str:
        return f'{self.title}'
    
class Files(models.Model):
    ads=models.ForeignKey(Ads, on_delete=models.CASCADE)
    name = models.CharField(verbose_name = 'Название файла')
    file = models.FileField(verbose_name='Файл', upload_to='docs/')
    date = models.DateTimeField(auto_now=timezone.now)
    def __str__(self) -> str:
        return f'{self.name}: ({self.date})'