from django.shortcuts import render
from .models import usuario

def lista_usuarios(request):
    return render(request, "usuarios/contacto.html")

