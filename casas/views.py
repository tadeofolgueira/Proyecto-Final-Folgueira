from django.shortcuts import render
from django.views.generic import ListView
from casas.models import casa

class casas(ListView):
    model = casa
    template_name = "casas/casas.html"
    context_object_name = "casas"
