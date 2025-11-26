from rest_framework import serializers
from .models import Lectura, RangoAlerta

class LecturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lectura
        fields = '__all__'

    # Validación personalizada
    def validate_ph(self, value):
        if not (0 <= value <= 14):
            raise serializers.ValidationError("El pH debe estar entre 0 y 14.")
        return value


class RangoAlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangoAlerta
        fields = '__all__'
