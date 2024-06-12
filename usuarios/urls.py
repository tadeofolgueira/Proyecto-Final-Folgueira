from django.urls import path
from .views import contacto, gracias

urlpatterns = [
    path("usuarios/", contacto, name="contacto"),
    path("", gracias, name="gracias"),
]