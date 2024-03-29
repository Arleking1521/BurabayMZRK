from django.contrib import admin
from .models import AntiCorruption
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(AntiCorruption)
class AnticorAdmin(TranslationAdmin):
    list_display = ( 'title', )