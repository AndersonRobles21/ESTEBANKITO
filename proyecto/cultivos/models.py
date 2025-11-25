from django.db import models

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)
    variedad = models.CharField(max_length=100, null=True, blank=True)
    etapa = models.CharField(max_length=100, null=True, blank=True)
    fecha_siembra = models.DateField()

    def __str__(self):
        return self.nombre
