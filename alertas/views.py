from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from datetime import timedelta

from .models import Alerta, ReglaAlerta
from .serializers import AlertaSerializer, ReglaAlertaSerializer


class ReglaAlertaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar reglas de alertas.
    
    Endpoints:
    - POST /api/alertas/reglas/ - Crear nueva regla
    - GET /api/alertas/reglas/ - Listar todas las reglas
    - GET /api/alertas/reglas/{id}/ - Obtener detalle de regla
    - PUT /api/alertas/reglas/{id}/ - Actualizar regla
    DELETE /api/alertas/reglas/{id}/ - Eliminar regla
    """
    queryset = ReglaAlerta.objects.all()
    serializer_class = ReglaAlertaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nombre', 'tipo_sensor']
    search_fields = ['nombre', 'condicion']
    ordering_fields = ['nombre', 'valor_umbral']


class AlertaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar alertas.
    
    Endpoints:
    - POST /api/alertas/alertas/ - Crear nueva alerta
    - GET /api/alertas/alertas/ - Listar todas las alertas
    - GET /api/alertas/alertas/{id}/ - Obtener detalle de alerta
    - PUT /api/alertas/alertas/{id}/ - Actualizar alerta
    - DELETE /api/alertas/alertas/{id}/ - Eliminar alerta
    - GET /api/alertas/alertas/filtrar-por-rango/ - Filtrar alertas por rango de fechas
    - GET /api/alertas/alertas/resumen-diario/ - Obtener resumen de alertas
    """
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['sensor', 'regla', 'activa']
    search_fields = ['mensaje', 'sensor__nombre']
    ordering_fields = ['fecha', 'sensor']
    ordering = ['-fecha']

    @action(detail=False, methods=['get'])
    def filtrar_por_rango(self, request):
        """
        Filtrar alertas por rango de fechas.
        
        Parámetros:
        - fecha_inicio: YYYY-MM-DD
        - fecha_fin: YYYY-MM-DD
        """
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')

        if not fecha_inicio or not fecha_fin:
            return Response({
                'error': 'Se requieren parámetros fecha_inicio y fecha_fin (YYYY-MM-DD)'
            }, status=400)

        try:
            from datetime import datetime
            inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        except ValueError:
            return Response({'error': 'Formato de fecha inválido. Use YYYY-MM-DD'}, status=400)

        alertas = self.queryset.filter(fecha__range=[inicio, fin])
        serializer = self.get_serializer(alertas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def resumen_diario(self, request):
        """
        Obtener resumen de alertas del día actual.
        """
        hoy = timezone.now().date()
        alertas_hoy = self.queryset.filter(fecha__date=hoy)

        resumen = {
            'fecha': hoy,
            'total_alertas': alertas_hoy.count(),
            'alertas_activas': alertas_hoy.filter(activa=True).count(),
            'alertas_inactivas': alertas_hoy.filter(activa=False).count(),
            'por_sensor': {}
        }

        for sensor_id in alertas_hoy.values_list('sensor_id', flat=True).distinct():
            sensor_nombre = alertas_hoy.filter(sensor_id=sensor_id).first().sensor.nombre
            resumen['por_sensor'][sensor_nombre] = alertas_hoy.filter(sensor_id=sensor_id).count()

        return Response(resumen)
