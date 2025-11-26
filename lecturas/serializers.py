from rest_framework import serializers
from .models import Lectura
from sensores.serializers import SensorSerializer
from sensores.models import Sensor


class LecturaSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer(read_only=True)
    sensor_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Sensor.objects.all(),
        source='sensor'
    )

    class Meta:
        model = Lectura
        fields = ['id', 'sensor', 'sensor_id', 'tipo_lectura', 'valor', 'fecha', 'unidad_medida']
        read_only_fields = ['fecha']

    def validate_valor(self, value):
        if value < 0:
            raise serializers.ValidationError("El valor de la lectura no puede ser negativo.")
        return value

    def validate(self, data):
        tipo_lectura = data.get('tipo_lectura')
        valor = data.get('valor')

        # Validaciones según el tipo de lectura
        if tipo_lectura == 'temperatura' and valor > 60:
            raise serializers.ValidationError("La temperatura no debe superar 60°C")
        elif tipo_lectura == 'humedad' and valor > 100:
            raise serializers.ValidationError("La humedad no puede superar 100%")
        elif tipo_lectura == 'pH' and (valor < 0 or valor > 14):
            raise serializers.ValidationError("El pH debe estar entre 0 y 14")

        return data
