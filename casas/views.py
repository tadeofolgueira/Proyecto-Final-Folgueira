from django.shortcuts import render
from django.views.generic import ListView
from casas.models import Casa
from .forms import BusquedaCasas
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

class Casas(ListView):
    model = Casa
    template_name = "casas/casas.html"
    context_object_name = "casas"


    def get_queryset(self):
        tipo = self.request.GET.get("tipo","")
        casas = self.model.objects.filter(tipo__icontains=tipo)
        return casas
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaCasas()
        context["tipo"] = self.request.GET.get("tipo","") 
        return context
        

class CrearCasa(CreateView):
    model = Casa
    template_name = "casas/crear_casa.html"
    success_url = reverse_lazy("casas")
    fields = ["tipo","estilo","inmoviliaria","fecha"]
    
class BorrarCasa(DeleteView):
    model = Casa 
    template_name = "casas/borrar_casa.html"
    success_url = reverse_lazy("casas")
    
class ActualizarCasa(UpdateView):
    model = Casa
    template_name = "casas/actualizar_casa.html"
    success_url = reverse_lazy("casas")
    fields = ["tipo","estilo","inmoviliaria","fecha"]
    
class VerCasa(DetailView):
    model = Casa
    template_name = "casas/ver_casa.html"


