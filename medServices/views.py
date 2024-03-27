from django.shortcuts import render
from .models import MedServices
# Create your views here.
def medServices(request):
    file = MedServices.objects.order_by('-id').first()
    return render(request, 'medServices/medServices.html', {'file':file})