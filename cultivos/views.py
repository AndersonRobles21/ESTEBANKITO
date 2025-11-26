from rest_framework import viewsets
from .models import Cultivo
from .serializers import CultivoSerializer

class CultivoViewSet(viewsets.ModelViewSet):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer
