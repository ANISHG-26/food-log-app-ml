from django.urls import path, include
from rest_framework import routers
from .viewsets import UploadedImagesViewSet
from .views import predicted_result
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('images', UploadedImagesViewSet, 'images')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('predict', predicted_result),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)