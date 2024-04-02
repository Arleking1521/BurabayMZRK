from django.contrib import admin
from .models import Ads, Files
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Ads)
class AdsAdmin(TranslationAdmin):
    list_display = ( 'title',)


@admin.register(Files)
class FilesAdmin(TranslationAdmin):
    list_display = ( 'name',)