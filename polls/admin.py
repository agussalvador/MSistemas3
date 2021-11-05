from django.contrib import admin

# Register your models here.
from polls.models import MyUser, Task, Category, Board

admin.site.register(MyUser)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Board)
