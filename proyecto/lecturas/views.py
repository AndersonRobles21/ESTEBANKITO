from django.shortcuts import render
from django.db.models import Avg
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Lectura, RangoAlerta
from .serializers import LecturaSerializer, RangoAlertaSerializer
from .filters import LecturaFilter

class LecturaViewSet(viewsets.ModelViewSet):
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LecturaFilter

    # ENDPOINT ADICIONAL (OBLIGATORIO)
    @action(detail=False, methods=["get"])
    def promedio(self, request):
        data = {
            "temperatura_promedio": Lectura.objects.all().aggregate(models.Avg('temperatura'))['temperatura__avg'],
            "humedad_promedio": Lectura.objects.all().aggregate(models.Avg('humedad'))['humedad__avg'],
            "ph_promedio": Lectura.objects.all().aggregate(models.Avg('ph'))['ph__avg']
        }
        return Response(data)


class RangoAlertaViewSet(viewsets.ModelViewSet):
    queryset = RangoAlerta.objects.all()
    serializer_class = RangoAlertaSerializer

