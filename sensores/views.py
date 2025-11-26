from django.shortcuts import render

from rest_framework import viewsets
from .models import TipoSensor, Sensor
from .serializers import TipoSensorSerializer, SensorSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TipoSensorViewSet(viewsets.ModelViewSet):
    queryset = TipoSensor.objects.all()
    serializer_class = TipoSensorSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['activo', 'tipo'] 
