from django.shortcuts import render
from .models import OrgStruct
# Create your views here.
def orgStruct(request):
    try:
        file = OrgStruct.objects.order_by('-id').first()
    except:
        file = None
    return render(request, 'orgStructure/orgStruct.html', {'file':file})