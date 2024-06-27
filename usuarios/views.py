from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as login_django
from .models import usuario
from .forms import ContactoForm, Registro

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

def login(request):
    formulario = AuthenticationForm()
    
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.cleaned_data.get("username")
            contrasenia = formulario.cleaned_data.get("password")
            
            users = authenticate(username=user, password=contrasenia)
            login_django(request,users)
            return redirect ("inicio")
    
    return render(request, "usuarios/login.html", {"formulario":formulario})

def registro(request):
    formulario = Registro()
    
    if request.method == "POST":
        formulario = Registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    return render(request, "usuarios/registro.html", {"formulario":formulario})


