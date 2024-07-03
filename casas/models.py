from django.db import models
from django.contrib.auth.models import User

class Casa(models.Model):
    tipo = models.CharField(max_length=20,default="Casa")
    estilo = models.CharField(max_length=20)
    inmoviliaria = models.CharField(max_length=20)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='casas/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.tipo.capitalize()} {self.estilo} - {self.inmoviliaria} ({self.fecha})"