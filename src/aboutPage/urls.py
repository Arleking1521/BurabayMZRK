from django.urls import path
from . import views

urlpatterns = [
    path('', views.aboutInfo, name = 'about'),
]