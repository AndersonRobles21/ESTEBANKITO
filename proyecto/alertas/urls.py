from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlertaViewSet, TipoAlertaViewSet

router = DefaultRouter()
router.register(r'tipos', TipoAlertaViewSet)
router.register(r'', AlertaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
