from django.contrib import admin
from .models import Post
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ( 'title', 'content')