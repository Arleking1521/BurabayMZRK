from modeltranslation.translator import register, TranslationOptions
from .models import Ads, Files

@register(Ads)
class AdsTranslationoptions(TranslationOptions):
    fields = ( 'title',)

@register(Files)
class FilesTranslationoptions(TranslationOptions):
    fields = ( 'name',)