
from django.contrib import admin
from django.urls import path
from . import views;

urlpatterns = [
    path('', views.addTask, name='addTaskPage'),
    path('add/', views.addTask, name='tasksPage')
]
