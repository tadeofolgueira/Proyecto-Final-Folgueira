from django.shortcuts import render

from .models import Modelo


def inicio(request):
    return render(request, "inicio/inicio.html")

def about(request):
    return render(request, "inicio/about.html")