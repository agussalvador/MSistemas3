"""Tpfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from boards import views
from boards.views import GenericCreateTask, GenericCreateCategory, GenericUpdateTask, GenericDeleteTask
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/board/', views.board, name='board'),
    path('register/', v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    # Task urls
    path('createtask', GenericCreateTask.as_view()),
    path('createcategory', GenericCreateCategory.as_view()),
    path('updatetask/<pk>', GenericUpdateTask.as_view()),
    path('deletetask/<pk>', GenericDeleteTask.as_view())

]
