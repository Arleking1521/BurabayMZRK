from django.db import models

# Create your models here.
class Managers(models.Model):
    name = models.CharField(max_length=128, verbose_name='Name') 
    post = models.TextField(verbose_name='Post')
    phone = models.CharField(verbose_name='Phone number')
    email = models.CharField(verbose_name='E-mail')
    reception = models.TextField(verbose_name='Day and time of reception', default = "none")
    show = models.BooleanField(verbose_name='Show this person in second table?')

    def __str__ (self) -> str:
        return f'{self.name}: {self.post}'
    
class Contacts(models.Model):
    title = models.CharField(verbose_name='Title')
    info = models.TextField(verbose_name='Information')

    def __str__ (self) -> str:
        return f'{self.title}: {self.info}'