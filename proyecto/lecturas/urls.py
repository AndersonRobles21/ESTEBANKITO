from rest_framework.routers import DefaultRouter
from .views import LecturaViewSet, RangoAlertaViewSet

router = DefaultRouter()
router.register('lecturas', LecturaViewSet)
router.register('rangos', RangoAlertaViewSet)

urlpatterns = router.urls
