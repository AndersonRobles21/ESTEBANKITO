from django.contrib import admin
from .models import Alerta, ReglaAlerta


@admin.register(ReglaAlerta)
class ReglaAlertaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'valor_umbral', 'tipo_sensor')


@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
	list_display = ('mensaje', 'sensor', 'regla', 'fecha', 'activa')
