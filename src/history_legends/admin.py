from django.contrib import admin
from .models import History
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    list_display = ( 'title', 'info')