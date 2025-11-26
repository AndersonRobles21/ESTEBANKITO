from django.db import models
from sensores.models import Sensor, TipoSensor
from cultivos.models import Cultivo


class TipoAlerta(models.Model):
    """Define los tipos de alertas disponibles en el sistema"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    nivel = models.CharField(
        max_length=20,
        choices=[
            ('CRITICO', 'Crítico'),
            ('ADVERTENCIA', 'Advertencia'),
            ('INFO', 'Información')
        ],
        default='INFO'
    )

    def __str__(self):
        return self.nombre


class Alerta(models.Model):
    """Modelo para registrar alertas generadas por condiciones anormales"""
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='alertas')
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='alertas')
    tipo_alerta = models.ForeignKey(TipoAlerta, on_delete=models.CASCADE, related_name='alertas')
    
    descripcion = models.TextField()
    valor_medido = models.FloatField()
    valor_limite = models.FloatField()
    
    estado = models.CharField(
        max_length=20,
        choices=[
            ('ACTIVA', 'Activa'),
            ('RESUELTA', 'Resuelta'),
            ('IGNORADA', 'Ignorada')
        ],
        default='ACTIVA'
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"Alerta {self.tipo_alerta} - {self.sensor.nombre}"
