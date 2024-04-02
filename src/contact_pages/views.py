from django.shortcuts import render
from .models import Managers, Contacts
# Create your views here.

def managerPostList(request):
    managers = Managers.objects.all()
    contacts = Contacts.objects.all()
    return render(request, 'infoPages/contacts.html', {'managers': managers, 'contacts': contacts})
