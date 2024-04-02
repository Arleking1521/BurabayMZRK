from django.shortcuts import render
from .models import WorkersInfo
# Create your views here.

def workersInfo(request):
    workers = WorkersInfo.objects.all()
    workers_list=[]
    for worker in workers:
        worker_data  = {
            'name':worker.name if workers else None,
            'post':worker.post if workers else None,
            'work_exp': worker.work_exp if workers else None,
            'sertificates':worker.sertificates.split('\n') if workers else None,
        }
        workers_list.append(worker_data)
    return render(request, 'infoPages/workersInfo.html', {'workers': workers_list })
