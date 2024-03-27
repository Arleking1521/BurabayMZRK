from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name = 'reviews'),
    path('new-review/', views.add_review, name = 'add-review'),
    path('<int:rid>/new-answer/', views.add_answer, name = 'add-answer'),
]