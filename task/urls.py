
from django.contrib import admin
from django.urls import path
from . import views;

urlpatterns = [
    path('', views.tasks, name='tasksPage'),
    path('add/', views.addTask, name='addTaskPage'),
    path('markComplete/<int:id>', views.markComplete ,name="markComplete"),
    path('deleteTask/<int:id>', views.deleteTask, name="deleteTask")
]
