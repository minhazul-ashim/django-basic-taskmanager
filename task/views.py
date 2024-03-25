from django.shortcuts import render, redirect;
from . import forms;
from .models import TaskModel;

# Create your views here.
def addTask(request) :
    form = forms.TaskForm;
    if request.method == 'POST' :
        form = forms.TaskForm(request.POST);
        if(form.is_valid()) :
            form.save();
            return redirect('tasksPage')
    else :
        form = forms.TaskForm();
    return render(request, 'addTask.html', {"form": form})

def tasks(request) :
    data = TaskModel.objects.all();
    return render(request, 'tasks.html', {"data" : data})

def markComplete(request, id) :
    task = TaskModel.objects.get(pk=id);
    task.isCompleted = True;
    task.save();
    return redirect('tasksPage')

def deleteTask(request, id) :
    task = TaskModel.objects.get(pk=id).delete();
    return redirect('tasksPage')
