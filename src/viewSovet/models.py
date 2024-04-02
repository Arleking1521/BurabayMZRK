from django.db import models

# Create your models here.

class ViewSovet(models.Model):
    title = models.CharField(verbose_name = 'Название')
    file = models.FileField(verbose_name='Документ', upload_to='docs/')

    def __str__(self) -> str:
        return f'{self.title}: {self.file}'