from django.contrib import admin
from .models import Vacancies, CompetitionInfo
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Vacancies)
class VacanciesAdmin(TranslationAdmin):
    list_display = ( 'vacancy', 'requirement')

@admin.register(CompetitionInfo)
class CompetitionInfoAdmin(TranslationAdmin):
    list_display = ( 'compAddress', 'enterpriseAddress', 'description', 'addmisions', 'documents', 'additionally')