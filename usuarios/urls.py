from django.urls import path
from usuarios import views

urlpatterns = [
    path("/listado",views.lista_usuarios),
]