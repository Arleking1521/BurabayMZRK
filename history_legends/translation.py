from modeltranslation.translator import register, TranslationOptions
from .models import History

@register(History)
class HistoryTranslationoptions(TranslationOptions):
    fields = ( 'title', 'info')