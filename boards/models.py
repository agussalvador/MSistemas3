from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Task(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=now)
    states = [
        ('To-Do', 'To-Do task'),
        ('In Progress', 'In progress task'),
        ('Finished', 'Task as finish'),
    ]
    state = models.CharField(max_length=15, choices=states, default='To-Do')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
