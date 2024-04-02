from django.contrib import admin
from .models import ViewSovet
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(ViewSovet)
class ViewSovetAdmin(TranslationAdmin):
    list_display = ( 'title', )