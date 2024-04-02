from django.shortcuts import render
from .models import Ads, Files
# Create your views here.
def ads(request):
    ads = Ads.objects.all()
    for ad in ads:
        files = Files.objects.filter(ads_id = ad.pk)
        ad.files = files
    return render(request, 'infoPages/advertisement.html', {'ads':ads})
