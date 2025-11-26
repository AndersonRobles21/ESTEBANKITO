from rest_framework.routers import DefaultRouter
from .views import AlertaViewSet, ReglaAlertaViewSet

router = DefaultRouter()
router.register('alertas', AlertaViewSet)
router.register('reglas', ReglaAlertaViewSet)

urlpatterns = router.urls
