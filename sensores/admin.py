from django.contrib import admin
from .models import TipoSensor, Sensor

@admin.register(TipoSensor)
class TipoSensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'fecha_instalacion', 'activo')
    list_filter = ('tipo', 'activo')
