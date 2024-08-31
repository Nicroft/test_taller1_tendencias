from rest_framework.routers import DefaultRouter
from ..libro.views import *

router = DefaultRouter()
 
router.register(r'libro', LibroViewSet, basename='libro')

urlpatterns = router.urls