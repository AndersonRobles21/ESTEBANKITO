from rest_framework import serializers
from .models import TipoSensor, Sensor
from datetime import date

class TipoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSensor
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    tipo = TipoSensorSerializer(read_only=True)
    tipo_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoSensor.objects.all(),
        source='tipo',
        write_only=True
    )  

    class Meta:
        model = Sensor
        fields = ['id', 'nombre', 'tipo', 'tipo_id', 'fecha_instalacion', 'activo']

    def validate_fecha_instalacion(self, value):
        if value > date.today():
            raise serializers.ValidationError("La fecha de instalación no puede ser futura.")
        return value