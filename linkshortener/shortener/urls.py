from rest_framework import routers
from .api import LinkViewSet


router = routers.DefaultRouter()
router.register('api/links', LinkViewSet, 'links')

urlpatterns = router.urls