from django.db import models

class casa(models.Model):
    estilo = models.CharField(max_length=20)
    inmoviliaria = models.CharField(max_length=20)
    fecha = models.DateField()

    def __str__(self):
        return f"Casa estilo {self.estilo} de la inmoviliaria {self.inmoviliaria}"