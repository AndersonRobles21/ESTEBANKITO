import django_filters
from .models import Lectura

class LecturaFilter(django_filters.FilterSet):
    fecha_min = django_filters.DateTimeFilter(field_name="fecha", lookup_expr='gte')
    fecha_max = django_filters.DateTimeFilter(field_name="fecha", lookup_expr='lte')
    ph_min = django_filters.NumberFilter(field_name="ph", lookup_expr='gte')
    temperatura_min = django_filters.NumberFilter(field_name="temperatura", lookup_expr='gte')

    class Meta:
        model = Lectura
        fields = ['sensor', 'fecha_min', 'fecha_max', 'ph_min', 'temperatura_min']

