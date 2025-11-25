from django.db import models

class TipoSensor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Sensor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoSensor, on_delete=models.CASCADE, related_name='sensores')
    fecha_instalacion = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre