from django.contrib import admin
from .models import AboutInfo
from modeltranslation.admin import TranslationAdmin
# Register your models here.

@admin.register(AboutInfo)
class AboutAdmin(TranslationAdmin):
    list_display = ( 'About', 'LDO')