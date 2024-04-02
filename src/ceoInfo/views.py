from django.shortcuts import render

from .models import CeoDatas, Education

# Create your views here.
def ceoInfo(request):
    datas = CeoDatas.objects.order_by('-id').first()
    edus = Education.objects.filter(ceo_id = datas.pk) if datas else []
 
    edus_list = []
    for edu in edus:
        edu_struct = {
            'university': edu.university,
            'info': edu.info.split('\n'),
        }
        edus_list.append(edu_struct)
    ceo_data = {
        'name': datas.name if datas else None,
        'date_of_birth' : datas.dateOfBirth if datas else None,
        'edu_parts': edus_list if edus else None,
        'spec_parts':  datas.scientific.split('\n') if datas else None,
        'work_parts':  datas.work_ex.split('\n') if datas else None,
        'add_parts':  datas.additionally.split('\n') if datas else None,
        'awards_parts':  datas.awards.split('\n') if datas else None,
        'sertif_parts':  datas.sertificates.split('\n') if datas else None,
        'public_parts':  datas.publications.split('\n') if datas else None,
        'photo': datas.photo if datas else None,
    }
    return render(request, 'ceoInfo/ceoInfoPage.html', {'datas': ceo_data})
