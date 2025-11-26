import django_filters
from .models import Cultivo

class CultivoFilter(django_filters.FilterSet):
    estado = django_filters.CharFilter(lookup_expr="iexact")
    fecha_siembra = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Cultivo
        fields = ["estado", "fecha_siembra"]
