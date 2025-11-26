from django.db import models
from sensores.models import Sensor  # si existe

class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='lecturas')
    temperatura = models.FloatField()
    humedad = models.FloatField()
    ph = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lectura {self.id} - Sensor {self.sensor_id}"


class RangoAlerta(models.Model):
    tipo = models.CharField(max_length=50)  # temperatura, humedad, ph
    minimo = models.FloatField()
    maximo = models.FloatField()

    def __str__(self):
        return f"{self.tipo}: {self.minimo} - {self.maximo}"
