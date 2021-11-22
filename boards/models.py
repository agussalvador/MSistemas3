from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


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

@receiver(pre_save, sender=Task)
def pre_save_task(sender, instance, **kwargs):
    if not instance._state.adding:
        print('Se actualizo una Tarea')
    else:
        print('Se agrego una nueva Tarea')


@receiver(pre_delete, sender=Task)
def pre_delete_task(sender, instance, **kwargs):
   print('Tarea eliminada')