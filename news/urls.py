from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'news'),
    path('<int:pid>/', views.post_detail, name = 'new_detail'),
    # path('new/', views.post_new, name='new_new'),
    path('<int:pid>/edit/', views.post_edit, name='new_edit'),
]