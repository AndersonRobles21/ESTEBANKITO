from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils import timezone

from .models import Alerta, TipoAlerta
from .serializers import AlertaSerializer, AlertaDetailSerializer, TipoAlertaSerializer
from .filters import AlertaFilter


class TipoAlertaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar tipos de alertas
    
    - POST /api/alertas/tipos/: Crear tipo de alerta
    - GET /api/alertas/tipos/: Listar tipos de alertas
    - GET /api/alertas/tipos/{id}/: Obtener detalle de tipo
    - PUT /api/alertas/tipos/{id}/: Actualizar tipo
    - DELETE /api/alertas/tipos/{id}/: Eliminar tipo
    """
    queryset = TipoAlerta.objects.all()
    serializer_class = TipoAlertaSerializer
    permission_classes = [AllowAny]


class AlertaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar alertas
    
    Endpoints:
    - POST /api/alertas/: Crear alerta
    - GET /api/alertas/: Listar alertas (con filtros)
    - GET /api/alertas/{id}/: Obtener detalle de alerta
    - PUT /api/alertas/{id}/: Actualizar alerta
    - PATCH /api/alertas/{id}/: Actualizar parcialmente
    - DELETE /api/alertas/{id}/: Eliminar alerta
    - GET /api/alertas/estadisticas/por_estado/: Estadísticas por estado
    - POST /api/alertas/{id}/resolver/: Marcar alerta como resuelta
    """
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AlertaFilter
    search_fields = ['descripcion', 'sensor__nombre', 'cultivo__nombre']
    ordering_fields = ['fecha_creacion', 'valor_medido', 'estado']
    ordering = ['-fecha_creacion']

    def get_serializer_class(self):
        """Usar serializer detallado para retrieve"""
        if self.action == 'retrieve':
            return AlertaDetailSerializer
        return AlertaSerializer

    @action(detail=True, methods=['post'])
    def resolver(self, request, pk=None):
        """
        Endpoint para marcar una alerta como resuelta
        POST /api/alertas/{id}/resolver/
        """
        alerta = self.get_object()
        
        if alerta.estado == 'RESUELTA':
            return Response(
                {'detail': 'La alerta ya está resuelta'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        alerta.estado = 'RESUELTA'
        alerta.fecha_resolucion = timezone.now()
        alerta.save()
        
        serializer = self.get_serializer(alerta)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def estadisticas(self, request):
        """
        Endpoint para obtener estadísticas generales
        GET /api/alertas/estadisticas/
        """
        total = Alerta.objects.count()
        activas = Alerta.objects.filter(estado='ACTIVA').count()
        resueltas = Alerta.objects.filter(estado='RESUELTA').count()
        ignoradas = Alerta.objects.filter(estado='IGNORADA').count()
        
        return Response({
            'total': total,
            'activas': activas,
            'resueltas': resueltas,
            'ignoradas': ignoradas,
            'porcentaje_activas': round((activas / total * 100) if total > 0 else 0, 2)
        })

    @action(detail=False, methods=['get'])
    def por_estado(self, request):
        """
        Endpoint para agrupar alertas por estado
        GET /api/alertas/por_estado/
        """
        estados = Alerta._meta.get_field('estado').choices
        resultado = {}
        
        for valor, etiqueta in estados:
            resultado[valor] = {
                'etiqueta': etiqueta,
                'cantidad': Alerta.objects.filter(estado=valor).count(),
                'alertas': AlertaSerializer(
                    Alerta.objects.filter(estado=valor),
                    many=True
                ).data
            }
        
        return Response(resultado)

    @action(detail=False, methods=['get'])
    def por_tipo(self, request):
        """
        Endpoint para agrupar alertas por tipo
        GET /api/alertas/por_tipo/
        """
        tipos = TipoAlerta.objects.all()
        resultado = []
        
        for tipo in tipos:
            resultado.append({
                'tipo_id': tipo.id,
                'tipo_nombre': tipo.nombre,
                'cantidad': tipo.alertas.count(),
                'alertas': AlertaSerializer(tipo.alertas.all(), many=True).data
            })
        
        return Response(resultado)

    @action(detail=False, methods=['get'])
    def criticas(self, request):
        """
        Endpoint para obtener solo alertas críticas activas
        GET /api/alertas/criticas/
        """
        alertas_criticas = Alerta.objects.filter(
            tipo_alerta__nivel='CRITICO',
            estado='ACTIVA'
        )
        serializer = self.get_serializer(alertas_criticas, many=True)
        return Response({
            'cantidad': alertas_criticas.count(),
            'alertas': serializer.data
        })

