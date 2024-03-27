from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewSovet, name = 'viewSovet'),
    path('<int:fid>/', views.file_detail, name = 'doc-detils'),
]