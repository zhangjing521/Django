from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='vocabulary.index'),
    path('add/', views.add_word, name='vocabulary.add')
]
