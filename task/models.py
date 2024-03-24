from django.db import models

# Create your models here.
class TaskModel(models.Model) :
    title = models.CharField(max_length = 100);
    description = models.CharField(max_length = 1000);
    isCompleted = models.BooleanField(default = False);
    assignDate = models.DateField();