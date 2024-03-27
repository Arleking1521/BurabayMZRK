from django.urls import path
from . import views

urlpatterns = [
    path('', views.medServices, name = 'med-services'),
]