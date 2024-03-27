from django.shortcuts import render
from .models import AboutInfo
# Create your views here.
def aboutInfo(request):
    datas = AboutInfo.objects.order_by('-id').first()
    data_part={
        'about': datas.About.split('\n') if datas else None,
        'ldo': datas.LDO.split('\n') if datas else None,
        'file': datas.file if datas else None,
    }
    return render(request, 'infoPages/aboutPage.html', {'datas':data_part})
