from django.urls import path
from . import views

urlpatterns = [
    path('', views.ceoInfo, name = 'ceo-info'),
]