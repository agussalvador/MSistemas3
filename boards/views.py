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
                  'board.html',
                  {'tasks': Task.objects.all()}
                  )


class GenericCreateCategory(CreateView):
    model = Category
    fields = ['name']
    template_name = 'form.html'
    success_url = '/login/board'


class GenericCreateTask(CreateView):
    model = Task
    fields = ['name', 'category']
    template_name = 'form.html'
    success_url = '/login/board'

    def form_valid(self, form):  # asigna el usuario que crea la Task, al objeto task
        form.instance.user = self.request.user
        return super(GenericCreateTask, self).form_valid(form)


class GenericUpdateTask(UpdateView):
    model = Task
    fields = ['name', 'category', 'state']
    template_name = 'form.html'
    success_url = '/login/board'


class GenericDeleteTask(DeleteView):
    model = Task
    success_url = '/login/board'
