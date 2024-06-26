from django.db import models
from task.models import TaskModel;

# Create your models here.
class TaskCategoryModel(models.Model) :
    name = models.CharField(max_length = 100);
    tasks = models.ManyToManyField(TaskModel);