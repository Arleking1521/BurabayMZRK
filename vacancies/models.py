from django.db import models
from django.forms import ValidationError

# Create your models here.
class Vacancies(models.Model):

    vacancy = models.TextField(verbose_name = 'Вакансия')
    requirement = models.TextField(verbose_name = 'Требования')

    def __str__ (self) -> str:
        return f'{self.vacancy}'
    
class CompetitionInfo(models.Model):
    compAddress = models.TextField(verbose_name = 'Адрес конкурса')
    enterpriseAddress = models.TextField(verbose_name = 'Адрес предприятия')
    description = models.TextField(verbose_name = 'Краткое описание')
    addmisions = models.TextField(verbose_name = 'Условия допуска к участию')
    documents = models.TextField(verbose_name = 'Список предоставляемсях документов')
    additionally = models.TextField(verbose_name = 'Дополнительная информация')


