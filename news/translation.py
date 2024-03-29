from modeltranslation.translator import register, TranslationOptions
from .models import Post

@register(Post)
class PostTranslationoptions(TranslationOptions):
    fields = ( 'title', 'content')