from django.db import models
from sensores.models import Sensor, TipoSensor   # tu FK y tipo

class ReglaAlerta(models.Model):
    nombre = models.CharField(max_length=100)
    condicion = models.CharField(max_length=100)   # ej: "temperatura > 35"
    valor_umbral = models.FloatField()
    tipo_sensor = models.ForeignKey(TipoSensor, on_delete=models.SET_NULL, null=True, blank=True,
                                    help_text="(opcional) aplicar regla solo a este tipo de sensor")

    def __str__(self):
        return self.nombre


class Alerta(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    regla = models.ForeignKey(ReglaAlerta, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"Alerta: {self.mensaje}"
