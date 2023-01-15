from django.urls import path, include

from .views import RecordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]