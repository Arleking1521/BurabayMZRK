from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacInfo_list, name = 'rules'),
]