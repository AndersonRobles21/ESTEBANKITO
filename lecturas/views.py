from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime, timedelta

from .models import Lectura
from .serializers import LecturaSerializer


class LecturaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar lecturas de sensores.
    
    Endpoints:
    - POST /api/lecturas/lecturas/ - Crear nueva lectura
    - GET /api/lecturas/lecturas/ - Listar todas las lecturas
    - GET /api/lecturas/lecturas/{id}/ - Obtener detalle de lectura
    - PUT /api/lecturas/lecturas/{id}/ - Actualizar lectura
    - DELETE /api/lecturas/lecturas/{id}/ - Eliminar lectura
    - GET /api/lecturas/lecturas/filtrar-por-rango/ - Filtrar por rango de fechas
    - GET /api/lecturas/lecturas/promedios-diarios/ - Obtener promedios diarios
    """
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['sensor', 'tipo_lectura']
    search_fields = ['sensor__nombre', 'tipo_lectura']
    ordering_fields = ['fecha', 'valor', 'sensor']
    ordering = ['-fecha']

    @action(detail=False, methods=['get'])
    def filtrar_por_rango(self, request):
        """
        Filtrar lecturas por rango de fechas.
        
        Parámetros:
        - fecha_inicio: YYYY-MM-DD
        - fecha_fin: YYYY-MM-DD
        - tipo_lectura: opcional (temperatura, humedad, pH, luminosidad)
        """
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        tipo_lectura = request.query_params.get('tipo_lectura')

        if not fecha_inicio or not fecha_fin:
            return Response({
                'error': 'Se requieren parámetros fecha_inicio y fecha_fin (YYYY-MM-DD)'
            }, status=400)

        try:
            inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fin = datetime.strptime(fecha_fin, '%Y-%m-%d') + timedelta(days=1)
        except ValueError:
            return Response({'error': 'Formato de fecha inválido. Use YYYY-MM-DD'}, status=400)

        lecturas = self.queryset.filter(fecha__range=[inicio, fin])
        
        if tipo_lectura:
            lecturas = lecturas.filter(tipo_lectura=tipo_lectura)

        serializer = self.get_serializer(lecturas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def promedios_diarios(self, request):
        """
        Obtener promedios diarios de lecturas.
        
        Parámetros:
        - dias: número de días para el cálculo (default: 7)
        - sensor_id: opcional, filtra por sensor específico
        """
        dias = int(request.query_params.get('dias', 7))
        sensor_id = request.query_params.get('sensor_id')
        
        fecha_inicio = datetime.now() - timedelta(days=dias)
        lecturas = self.queryset.filter(fecha__gte=fecha_inicio)

        if sensor_id:
            lecturas = lecturas.filter(sensor_id=sensor_id)

        promedios = {}
        for tipo in ['temperatura', 'humedad', 'pH', 'luminosidad']:
            lecturas_tipo = lecturas.filter(tipo_lectura=tipo)
            if lecturas_tipo.exists():
                promedio = sum(l.valor for l in lecturas_tipo) / lecturas_tipo.count()
                maximo = max(l.valor for l in lecturas_tipo)
                minimo = min(l.valor for l in lecturas_tipo)
                promedios[tipo] = {
                    'promedio': round(promedio, 2),
                    'maximo': maximo,
                    'minimo': minimo,
                    'total_lecturas': lecturas_tipo.count()
                }

        return Response({
            'periodo_dias': dias,
            'fecha_inicio': fecha_inicio.date(),
            'fecha_fin': datetime.now().date(),
            'promedios': promedios
        })

