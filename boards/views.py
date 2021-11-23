from abc import ABC

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from boards.models import Task, Category

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer


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
    fields = ['name', 'user', 'category']
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


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'name', 'creation_date', 'state', 'user', 'category'
        )


class TaskViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
