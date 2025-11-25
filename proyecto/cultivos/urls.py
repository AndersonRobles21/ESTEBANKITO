from rest_framework import routers
from .views import CultivoViewSet

router = routers.DefaultRouter()
router.register(r'cultivos', CultivoViewSet)

urlpatterns = router.urls
