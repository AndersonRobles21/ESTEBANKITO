from rest_framework.routers import DefaultRouter
from .views import TipoSensorViewSet, SensorViewSet

router = DefaultRouter()
router.register(r'tipos', TipoSensorViewSet)
router.register(r'sensores', SensorViewSet)

urlpatterns = router.urls
