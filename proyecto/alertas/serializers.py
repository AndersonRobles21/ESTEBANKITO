from rest_framework import serializers
from .models import Alerta, TipoAlerta


class TipoAlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAlerta
        fields = ['id', 'nombre', 'descripcion', 'nivel']


class AlertaSerializer(serializers.ModelSerializer):
    tipo_alerta_nombre = serializers.CharField(source='tipo_alerta.nombre', read_only=True)
    sensor_nombre = serializers.CharField(source='sensor.nombre', read_only=True)
    cultivo_nombre = serializers.CharField(source='cultivo.nombre', read_only=True)
    
    class Meta:
        model = Alerta
        fields = [
            'id', 'sensor', 'cultivo', 'tipo_alerta',
            'descripcion', 'valor_medido', 'valor_limite',
            'estado', 'fecha_creacion', 'fecha_resolucion',
            'tipo_alerta_nombre', 'sensor_nombre', 'cultivo_nombre'
        ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_resolucion']

    def validate(self, data):
        """Validaciones personalizadas"""
        # Validar que el valor medido y límite sean razonables
        if data.get('valor_medido') and data.get('valor_limite'):
            if data['valor_medido'] < 0 or data['valor_limite'] < 0:
                raise serializers.ValidationError(
                    "Los valores medido y límite deben ser positivos"
                )
        
        # Validar que el sensor esté activo
        sensor = data.get('sensor')
        if sensor and not sensor.activo:
            raise serializers.ValidationError(
                "No se puede crear alerta para un sensor inactivo"
            )
        
        return data


class AlertaDetailSerializer(AlertaSerializer):
    """Serializer ampliado con más detalles"""
    tipo_alerta = TipoAlertaSerializer(read_only=True)
    sensor_detalle = serializers.SerializerMethodField()
    cultivo_detalle = serializers.SerializerMethodField()
    
    class Meta(AlertaSerializer.Meta):
        fields = AlertaSerializer.Meta.fields + ['tipo_alerta', 'sensor_detalle', 'cultivo_detalle']
    
    def get_sensor_detalle(self, obj):
        return {
            'id': obj.sensor.id,
            'nombre': obj.sensor.nombre,
            'tipo': obj.sensor.tipo.nombre,
            'activo': obj.sensor.activo
        }
    
    def get_cultivo_detalle(self, obj):
        return {
            'id': obj.cultivo.id,
            'nombre': obj.cultivo.nombre,
            'variedad': obj.cultivo.variedad,
            'etapa': obj.cultivo.etapa
        }
