from django.db import models
from sensores.models import Sensor

class Lectura(models.Model):
    TIPO_LECTURA_CHOICES = [
        ('temperatura', 'Temperatura'),
        ('humedad', 'Humedad'),
        ('pH', 'pH'),
        ('luminosidad', 'Luminosidad'),
    ]

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='lecturas')
    tipo_lectura = models.CharField(max_length=50, choices=TIPO_LECTURA_CHOICES)
    valor = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)
    unidad_medida = models.CharField(max_length=20, default='')  # °C, %, pH, lux, etc.

    class Meta:
        ordering = ['-fecha']
        indexes = [
            models.Index(fields=['-fecha']),
            models.Index(fields=['sensor', '-fecha']),
        ]

    def __str__(self):
        return f"Lectura: {self.sensor.nombre} - {self.tipo_lectura}: {self.valor} {self.unidad_medida}"
