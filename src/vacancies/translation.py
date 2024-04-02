from modeltranslation.translator import register, TranslationOptions
from .models import Vacancies, CompetitionInfo

@register(Vacancies)
class VacanciesTranslationoptions(TranslationOptions):
    fields = ( 'vacancy', 'requirement')

@register(CompetitionInfo)
class CompetitionInfoTranslationoptions(TranslationOptions):
    fields = ( 'compAddress', 'enterpriseAddress', 'description', 'addmisions', 'documents', 'additionally')