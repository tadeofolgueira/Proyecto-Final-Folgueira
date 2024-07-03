from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
]


