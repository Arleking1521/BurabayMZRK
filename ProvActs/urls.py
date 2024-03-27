from django.urls import path
from . import views

urlpatterns = [
    path('', views.provActs, name = 'rights-acts'),
]