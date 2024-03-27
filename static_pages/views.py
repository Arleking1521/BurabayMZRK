from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'MainPage/index.html')

def site_map(request):
    return render(request, 'MainPage/site_map.html')

def messages(request):
    return render(request, 'MainPage/message.html')

def symbols(request):
    return render(request, 'MainPage/symbols.html')