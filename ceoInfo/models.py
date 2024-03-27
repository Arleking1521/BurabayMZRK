from django.db import models

# Create your models here.
class CeoDatas(models.Model):
    name = models.CharField(verbose_name = 'Имя руководителя')
    dateOfBirth = models.CharField(verbose_name = 'Дата рождания')
    scientific = models.TextField(verbose_name = 'Научная степень')
    work_ex = models.TextField(verbose_name = 'Опыт работы')
    additionally = models.TextField(verbose_name = 'Дополнительно')
    awards = models.TextField(verbose_name = 'Награды')
    sertificates = models.TextField(verbose_name = 'Сертификаты')
    publications = models.TextField(verbose_name = 'Публикации')
    photo = models.FileField(verbose_name= 'Фото руководителя', upload_to='images/')
    def __str__ (self) -> str:
        return f'{self.name}'
    
class Education(models.Model):
    ceo = models.ForeignKey(CeoDatas, on_delete = models.CASCADE)
    university = models.TextField(verbose_name = "Учебное учреждание")
    info = models.TextField(verbose_name = 'Информация об образование в данном учреждении')

    def __str__ (self) -> str:
        return f'{self.university}: {self.info}'
    
