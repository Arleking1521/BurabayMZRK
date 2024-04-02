from django.shortcuts import render
from .models import AntiCorruption
# Create your views here.
def antiCorList(request):
    files = AntiCorruption.objects.all()
    return render(request, 'antiCorPages/antiCorList.html', {'files':files})

def file_detail(request, fid):
    file = AntiCorruption.objects.get(id = fid)
    return render(request, 'antiCorPages/doc-details.html', {'file':file})