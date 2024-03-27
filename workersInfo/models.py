from django.db import models

# Create your models here.
class WorkersInfo(models.Model):
    name = models.CharField(max_length=128, verbose_name='ФИО') 
    post = models.TextField(verbose_name='Должность')
    work_exp = models.CharField(verbose_name = 'Стаж')
    sertificates = models.TextField(verbose_name = 'Сертификат специалиста')

    def __str__ (self) -> str:
        return f'{self.name}: {self.post}'
    