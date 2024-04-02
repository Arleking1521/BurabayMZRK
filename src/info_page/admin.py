from django.contrib import admin
from .models import PacientInfo
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(PacientInfo)
class PacientInfoAdmin(TranslationAdmin):
    list_display = ( 'title', 'info')