from django.urls import path
from . import views

urlpatterns = [
    path('', views.antiCorList, name = 'antiCor'),
    path('<int:fid>/', views.file_detail, name = 'antiCorDetails'),
]