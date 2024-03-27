from django.shortcuts import render
from .models import PacientInfo

# Create your views here.

def pacInfo_list(request):
    rules = PacientInfo.objects.all()
    rules_list = []
    for rule in rules:
        info_parts = rule.info.split('\n')
        rule_data = {
            'title': rule.title,
            'info_parts': info_parts
        }
        rules_list.append(rule_data)
    return render(request, 'infoPages/rulesPage.html', {'rules': rules_list})

