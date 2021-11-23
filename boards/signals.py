from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from boards.models import Task

@receiver(pre_save, sender=Task)
def pre_save_task(sender, instance, **kwargs):
    if not instance._state.adding:
        print('Se actualizo una Tarea')
    else:
        print('Se agrego una nueva Tarea')

@receiver(pre_delete, sender=Task)
def pre_delete_task(sender, instance, **kwargs):
    print('Tarea eliminada')
