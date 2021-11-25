import math

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from vacunatorios.models import Sede
from datetime import datetime
from django.contrib.auth import logout
import random
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
# Create your views here.


def index(request):
    return render(request, 'index.html')


def estado_actual(hora_inicio, hora_fin):
    ahora = datetime.now().time()
    estado = "Cerrado"

    if ahora > hora_inicio and ahora < hora_fin:
        estado = "Abierto"
    return estado


def sedes(request):
    sedes = Sede.objects.all()

    for sede in sedes:
        sede.estado = estado_actual(sede.hora_inicio, sede.hora_fin)
        promedio = promedio_tiempo_espera(sede.prom_llegadas, sede.prom_atendidas)

    return render(request, 'sedes.html', {'sedes': sedes, 'promedio': promedio})


def promedio_tiempo_espera(llegadas, atendidas):
    #promedio de llegadas por hora
    lamb = llegadas
    #promedio de atencion por hora
    mu = atendidas
    #tiempo promedio que una unidad espera en la cola
    wq = lamb / (mu * (mu - lamb))
    resultado = round(wq * 60)
    return resultado


@login_required
def sede_logeada(request):
    sedes = Sede.objects.all()

    for sede in sedes:
        if sede.user == request.user:
            sede.estado = estado_actual(sede.hora_inicio, sede.hora_fin)
            promedio = promedio_tiempo_espera(sede.prom_llegadas, sede.prom_atendidas)
            return render(request, 'sedeLogeada.html', {'sede': sede, 'promedio': promedio})


def logout_view(request):
    logout(request, 'index.html')

