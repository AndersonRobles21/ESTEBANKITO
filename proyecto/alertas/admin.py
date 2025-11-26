from django.contrib import admin
from .models import Alerta, TipoAlerta


@admin.register(TipoAlerta)
class TipoAlertaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nivel', 'descripcion']
    list_filter = ['nivel']
    search_fields = ['nombre']


@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'cultivo', 'tipo_alerta', 'estado', 'fecha_creacion']
    list_filter = ['estado', 'tipo_alerta', 'fecha_creacion']
    search_fields = ['sensor__nombre', 'cultivo__nombre', 'descripcion']
    readonly_fields = ['fecha_creacion', 'fecha_resolucion']
    fieldsets = (
        ('Información General', {
            'fields': ('sensor', 'cultivo', 'tipo_alerta', 'descripcion')
        }),
        ('Valores', {
            'fields': ('valor_medido', 'valor_limite')
        }),
        ('Estado', {
            'fields': ('estado', 'fecha_creacion', 'fecha_resolucion')
        }),
    )

