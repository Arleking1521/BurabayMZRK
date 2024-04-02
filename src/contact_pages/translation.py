from modeltranslation.translator import register, TranslationOptions
from .models import Managers, Contacts

@register(Managers)
class ManagersTranslationoptions(TranslationOptions):
    fields = ( 'name', 'post', 'reception')

@register(Contacts)
class ContactsTranslationoptions(TranslationOptions):
    fields = ( 'title', 'info')