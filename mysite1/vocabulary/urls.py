from django.contrib import admin
from django.urls import path
from vocabulary import views

urlpatterns = [
    path('index/', views.index),
    #单词管理
    path('info/list/', views.info_list),
]