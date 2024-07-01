from django.urls import path
from casas import views

urlpatterns = [
    path("casas/",views.Casas.as_view(), name="casas" ),
    path("casas/crear/",views.CrearCasa.as_view(), name="crear_casa" ),
    path("casas/<int:pk>/",views.VerCasa.as_view(), name="ver_casa" ),
    path("casas/<int:pk>/actualizar/",views.ActualizarCasa, name="actualizar_casa" ),
    path("casas/<int:pk>/borrar/",views.BorrarCasa, name="borrar_casa" ),
    
]
