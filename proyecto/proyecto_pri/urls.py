from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.shortcuts import render

def home(request):
    return render(request, "home.html")


schema_view = get_schema_view(
    openapi.Info(
        title="API Cultivos Inteligentes",
        default_version='v1',
        description="Documentación automática",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', home),  # ← ← ← ESTA ES LA QUE FALTABA
    path('admin/', admin.site.urls),
    path('api/', include('cultivos.urls')),
    path('api/', include('sensores.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]
