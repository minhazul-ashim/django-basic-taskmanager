from django.shortcuts import render
from . import forms;

# Create your views here.
def addTask(request) :
    form = forms.TaskForm;
    return render(request, 'addTask.html', {"form": form})
