from modeltranslation.translator import register, TranslationOptions
from .models import ViewSovet

@register(ViewSovet)
class ViewSovetTranslationoptions(TranslationOptions):
    fields = ( 'title', )

