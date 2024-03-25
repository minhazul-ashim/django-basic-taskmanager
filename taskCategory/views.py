from django.shortcuts import render, redirect;
from . import forms;

# Create your views here.
def add(request) :
    form = forms.TaskCategoryForms;
    if request.method == 'POST' :
        form = forms.TaskCategoryForms(request.POST);
        if(form.is_valid()) :
            form.save();
            return redirect('tasksPage')
    else :
        form = forms.TaskCategoryForms();
    return render(request, 'addCategory.html', {'form': form});