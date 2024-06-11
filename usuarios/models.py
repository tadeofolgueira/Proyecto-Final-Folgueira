from django.db import models

class usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    
def __str__(self):
    return f"Se registró el usuario {self.nombre} {self.apellido}"

