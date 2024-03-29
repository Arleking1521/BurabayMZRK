from django.contrib import admin
from .models import ProvActs
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(ProvActs)
class ProvActsAdmin(TranslationAdmin):
    list_display = ( 'description',)
