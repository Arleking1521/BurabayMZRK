from modeltranslation.translator import register, TranslationOptions
from .models import AntiCorruption

@register(AntiCorruption)
class AntiCorTranslationoptions(TranslationOptions):
    fields = ( 'title',)
