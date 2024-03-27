from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('site-map/', views.site_map, name = 'site_map'),
    path('symbols/', views.symbols, name = 'symbols'),
    path('messages/', views.messages, name = 'messages'),
]