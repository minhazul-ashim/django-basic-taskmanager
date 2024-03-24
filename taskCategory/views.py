from django.shortcuts import render
from . import forms;

# Create your views here.
def add(request) :
    form = forms.TaskCategoryForms;
    return render(request, 'addCategory.html', {'form': form});