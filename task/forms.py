from django import forms;
from .models import TaskModel

class TaskForm(forms.ModelForm) :
    class Meta :
        model = TaskModel;
        fields = "__all__";
        exclude = ["isCompleted"]
        widgets = {
            "assignDate": forms.DateInput(attrs={'type': 'date'}),
            "description": forms.Textarea(attrs={"rows": "4"})
        }