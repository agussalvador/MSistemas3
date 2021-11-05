from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    creation_date = models.DateTimeField
    states = [
        ('Finished','Task as finish'),
        ('In Progress','In progress task')
    ]
    state = models.CharField(max_length=15,choices=states,default='In Progress')
    finish_date = models.DateTimeField


class Category(models.Model):
     name = models.CharField(max_length=100)



class Board(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=15)
    country = models.CharField(max_length=100)

class MyUser(User):
    name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)
