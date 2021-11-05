from django.contrib.auth import authenticate, login
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def hello_world(request):
    return render(request,
                  'polls/index.html'
                  )

@csrf_exempt
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        ...
    else:
        ...


