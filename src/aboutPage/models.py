from django.db import models

# Create your models here.
class AboutInfo(models.Model):
    About = models.TextField(verbose_name = 'Описание')
    LDO = models.TextField(verbose_name = 'Лечебно-Диагностическое отделение')
    file = models.FileField(verbose_name='Файл с описанием', upload_to='docs/')

    def __str__ (self) -> str:
        return f'О НИИ Курортологии'

