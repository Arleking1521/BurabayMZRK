from django.shortcuts import render
from .models import History

# Create your views here.

def history_list(request):
    histories = History.objects.all()
    history_list = []
    for history in histories:
        info_parts = history.info.split('\n')
        history_data = {
            'title': history.title,
            'info_parts': info_parts
        }
        history_list.append(history_data)
    return render(request, 'infoPages/historyPage.html', {'histories': history_list})
