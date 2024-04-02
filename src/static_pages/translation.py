from modeltranslation.translator import register, TranslationOptions
from .models import index_page

@register(index_page)
class ProvActsTranslationoptions(TranslationOptions):
    fields = ( 'bannerContent', 'ceo_appeal')