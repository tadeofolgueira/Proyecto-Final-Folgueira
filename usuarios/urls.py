from django.urls import path
from usuarios import views
from .views import contacto, gracias, login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("usuarios/", contacto, name="contacto"),
    path("", gracias, name="gracias"),
    path("logout/", LogoutView.as_view(template_name="usuarios/logout.html") ,name="logout"),
    path("login/", views.login ,name="login"),
    path("registro/", views.registro ,name="registro"),
]