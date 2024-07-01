from django.db import models
from django.contrib.auth.models import User

class usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    
def __str__(self):
    return f"Se registró el usuario {self.nombre} {self.apellido}"

class DatosUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)
    