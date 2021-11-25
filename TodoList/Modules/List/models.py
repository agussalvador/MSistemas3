from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    comment = models.CharField(max_length=250)
    names = [
        ('Finish', 'Finish Task'),
        ('In Progress', 'Task in progress')
    ]
    state = models.CharField(max_length=20, choices=names, default='En progreso')

class Tags(models.Model):
    name = models.CharField(max_length=50)





