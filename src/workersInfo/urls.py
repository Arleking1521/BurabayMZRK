from django.urls import path
from . import views

urlpatterns = [
    path('', views.workersInfo, name = 'workers-info'),
]