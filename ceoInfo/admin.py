from django.contrib import admin
from .models import CeoDatas,Education
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(CeoDatas)
class CeoDatasAdmin(TranslationAdmin):
    list_display = ( 'name', 'dateOfBirth', 'scientific', 'work_ex', 'additionally', 'awards', 'sertificates', 'publications')

@admin.register(Education)
class EducationAdmin(TranslationAdmin):
    list_display = ( 'university', 'info')