from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import usuario, DatosUser
from .forms import ContactoForm, Registro, EditarPerfil, CambiarContrasenia

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
            
            DatosUser.objects.get_or_create(user=users)
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

@login_required
def editar_perfil(request):
    
    formulario = EditarPerfil(initial = {"avatar": request.user.datosuser.avatar,"sexo":request.user.datosuser.sexo}, instance=request.user)
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST,request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get("avatar")
            request.user.datosuser.avatar = avatar
            sexo = formulario.cleaned_data.get("sexo")
            request.user.datosuser.sexo = sexo
            request.user.datosuser.save()
            formulario.save()
            return redirect("editar_perfil")
    
    return render(request,"usuarios/editar_perfil.html",{"formulario":formulario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "usuarios/cambiar_contrasenia.html"
    success_url = reverse_lazy("editar_perfil")
    form_class = CambiarContrasenia