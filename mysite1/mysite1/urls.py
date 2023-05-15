from django.contrib import admin
from django.urls import path
from vocabulary import views

urlpatterns = [
    
    path('words/list/', views.words_list),
    path('words/translate/', views.words_translate),
    path('words/add/', views.words_add),
    path('words/model/form/add/', views.words_model_form_add),
    path('words/delete/', views.words_delete),
    path('words/<int:nid>/edit/', views.words_edit),
]
