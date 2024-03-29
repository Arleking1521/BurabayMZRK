from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import index_page
# Register your models here.

@admin.register(index_page)
class indexPageAdmin(TranslationAdmin):
    list_display = ( 'bannerContent', 'ceo_appeal')