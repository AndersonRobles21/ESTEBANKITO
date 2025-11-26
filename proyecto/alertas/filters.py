import django_filters
from .models import Alerta


class AlertaFilter(django_filters.FilterSet):
    """Filtros para la aplicación de alertas"""
    
    # Filtro por rango de fechas
    fecha_creacion_desde = django_filters.DateTimeFilter(
        field_name='fecha_creacion',
        lookup_expr='gte',
        label='Fecha creación desde'
    )
    fecha_creacion_hasta = django_filters.DateTimeFilter(
        field_name='fecha_creacion',
        lookup_expr='lte',
        label='Fecha creación hasta'
    )
    
    # Filtro por estado
    estado = django_filters.ChoiceFilter(
        choices=Alerta._meta.get_field('estado').choices,
        label='Estado de la alerta'
    )
    
    # Filtro por tipo de alerta
    tipo_alerta = django_filters.NumberFilter(
        field_name='tipo_alerta__id',
        label='ID del tipo de alerta'
    )
    
    # Filtro por sensor
    sensor = django_filters.NumberFilter(
        field_name='sensor__id',
        label='ID del sensor'
    )
    
    # Filtro por cultivo
    cultivo = django_filters.NumberFilter(
        field_name='cultivo__id',
        label='ID del cultivo'
    )
    
    # Filtro por rango de valores medidos
    valor_medido_desde = django_filters.NumberFilter(
        field_name='valor_medido',
        lookup_expr='gte',
        label='Valor medido mínimo'
    )
    valor_medido_hasta = django_filters.NumberFilter(
        field_name='valor_medido',
        lookup_expr='lte',
        label='Valor medido máximo'
    )
    
    class Meta:
        model = Alerta
        fields = ['estado', 'tipo_alerta', 'sensor', 'cultivo']
