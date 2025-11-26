from rest_framework import serializers
from .models import Alerta, ReglaAlerta
from sensores.models import Sensor
from sensores.serializers import SensorSerializer, TipoSensorSerializer


class ReglaAlertaSerializer(serializers.ModelSerializer):
    tipo_sensor = TipoSensorSerializer(read_only=True)
    tipo_sensor_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=__import__('sensores.models', fromlist=['TipoSensor']).TipoSensor.objects.all(),
        source='tipo_sensor',
        required=False,
        allow_null=True
    )

    class Meta:
        model = ReglaAlerta
        fields = ['id', 'nombre', 'condicion', 'valor_umbral', 'tipo_sensor', 'tipo_sensor_id']

    def validate_valor_umbral(self, value):
        if value < 0:
            raise serializers.ValidationError("El umbral no puede ser negativo.")
        return value

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre debe tener mínimo 3 caracteres.")
        return value

    def validate_condicion(self, value):
        operadores_validos = ['>', '<', '>=', '<=', '==', '!=']
        if not any(op in value for op in operadores_validos):
            raise serializers.ValidationError("La condición debe contener un operador válido (>, <, >=, <=, ==, !=)")
        return value


class AlertaSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(read_only=True)
    sensor_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Sensor.objects.all(),
        source='sensor'
    )
    regla = ReglaAlertaSerializer(read_only=True)
    regla_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=ReglaAlerta.objects.all(),
        source='regla'
    )

    class Meta:
        model = Alerta
        fields = ['id', 'sensor', 'sensor_id', 'regla', 'regla_id', 'mensaje', 'fecha', 'activa']
        read_only_fields = ['fecha']

    def validate_mensaje(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("El mensaje debe tener mínimo 5 caracteres.")
        if len(value) > 200:
            raise serializers.ValidationError("El mensaje no puede exceder 200 caracteres.")
        return value
