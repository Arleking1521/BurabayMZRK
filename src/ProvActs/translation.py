from modeltranslation.translator import register, TranslationOptions
from .models import ProvActs

@register(ProvActs)
class ProvActsTranslationoptions(TranslationOptions):
    fields = ( 'description',)