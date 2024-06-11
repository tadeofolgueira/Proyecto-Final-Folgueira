from django.db import models

class Modelo(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha = models.DateField()

def __str__(self):
    return self.titulo


