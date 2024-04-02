from modeltranslation.translator import register, TranslationOptions
from .models import PacientInfo

@register(PacientInfo)
class PacientInfoTranslationoptions(TranslationOptions):
    fields = ( 'title', 'info')