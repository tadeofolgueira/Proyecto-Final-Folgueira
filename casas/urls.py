from django.urls import path
from casas import views

urlpatterns = [
    path("casas/",views.casas.as_view(), name="casas" )
]
