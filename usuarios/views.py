from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactoForm
from .models import usuario 

def contacto(request):
    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data["nombre"]
            apellido = formulario.cleaned_data["apellido"]
            nuevo_usuario = usuario(nombre=nombre, apellido=apellido)
            nuevo_usuario.save()
            return HttpResponseRedirect("/gracias/")  
    else:
        formulario = ContactoForm()

    return render(request, "usuarios/contacto.html", {"form": formulario})

def gracias(request):
    usuarios = usuario.objects.all()
    return render(request, "usuarios/gracias.html",{"usuarios": usuarios})


