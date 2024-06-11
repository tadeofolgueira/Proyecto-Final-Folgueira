from django.shortcuts import render

from .models import Modelo as Modelo


def inicio(request):
    return render(request, "inicio/inicio.html")

