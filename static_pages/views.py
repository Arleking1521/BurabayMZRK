from django.shortcuts import render
from .models import index_page
from ceoInfo.models import CeoDatas
# Create your views here.

def index(request):
    content = index_page.objects.order_by('-id').first()
    ceo_datas = CeoDatas.objects.order_by('-id').first()
    return render(request, 'MainPage/index.html', {'content': content, "ceo": ceo_datas})

def site_map(request):
    return render(request, 'MainPage/site_map.html')

def messages(request):
    return render(request, 'MainPage/message.html')

def symbols(request):
    return render(request, 'MainPage/symbols.html')