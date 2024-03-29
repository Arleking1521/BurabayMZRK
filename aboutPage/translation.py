from modeltranslation.translator import register, TranslationOptions
from .models import AboutInfo

@register(AboutInfo)
class AboutTranslationoptions(TranslationOptions):
    fields = ( 'About', 'LDO')