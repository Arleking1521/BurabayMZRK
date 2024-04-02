from modeltranslation.translator import register, TranslationOptions
from .models import WorkersInfo

@register(WorkersInfo)
class WorkersInfoTranslationoptions(TranslationOptions):
    fields = ( 'post', 'sertificates')

