from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView

from boards.models import Task, Category


def index(request):
    return render(request, 'index.html')


@login_required
def board(request):
    return render(request,
                  'board2.html',
                  {'tasks': Task.objects.all()}
                  )


class GenericCreateCategory(CreateView):
    model = Category
    fields = ['name']
    template_name = 'form.html'
    success_url = '/'


class GenericCreateTask(CreateView):
    model = Task
    fields = ['name', 'category', 'user']
    template_name = 'form.html'
    success_url = '/login/board'


class GenericUpdateTask(UpdateView):
    model = Task
    fields = ['name', 'category', 'state']
    template_name = 'form.html'
    success_url = '/login/board'


class GenericDeleteTask(DeleteView):
    model = Task
    success_url = '/login/board'
