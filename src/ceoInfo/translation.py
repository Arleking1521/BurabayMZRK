from modeltranslation.translator import register, TranslationOptions
from .models import CeoDatas, Education

@register(CeoDatas)
class CeoDatasTranslationoptions(TranslationOptions):
    fields = ( 'name', 'dateOfBirth', 'scientific', 'work_ex', 'additionally', 'awards', 'sertificates', 'publications')

@register(Education)
class EducationsTranslationoptions(TranslationOptions):
    fields = ( 'university', 'info')
