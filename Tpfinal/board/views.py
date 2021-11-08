from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required
def board(request):
    return render(request, 'board.html')

