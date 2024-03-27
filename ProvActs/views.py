from django.shortcuts import render
from .models import ProvActs

# Create your views here.

def provActs(request):
    rights = ProvActs.objects.all()
    rights_list = []
    for right in rights:
        info_parts = right.description.split('\n')
        rights_data = {
            'info_parts': info_parts
        }
        rights_list.append(rights_data)
    return render(request, 'infoPages/rightActs.html', {'rights': rights_list})
