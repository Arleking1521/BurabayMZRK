from django.contrib import admin
from .models import WorkersInfo
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(WorkersInfo)
class WorkersInfoAdmin(TranslationAdmin):
    list_display = (  'post', 'sertificates')