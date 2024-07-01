from django.db import models

class Casa(models.Model):
    tipo = models.CharField(max_length=20,default="Desconocido")
    estilo = models.CharField(max_length=20)
    inmoviliaria = models.CharField(max_length=20)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.tipo.capitalize()} estilo {self.estilo} de la inmoviliaria {self.inmoviliaria}"