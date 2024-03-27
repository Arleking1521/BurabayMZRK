from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(verbose_name = 'Имя')
    surename = models.CharField(verbose_name = 'Фамилия')
    phone = models.CharField(verbose_name = 'Телефон')
    email = models.EmailField(unique=True, verbose_name = 'Почта' )
    password = models.CharField(max_length=128, verbose_name = 'Пароль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'surename']

    def __str__ (self) -> str:
        return f'{self.name} {self.surename}: {self.email}'
    

