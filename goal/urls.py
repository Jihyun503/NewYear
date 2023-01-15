from django.urls import path, include

from .views import GoalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('', GoalViewSet)

urlpatterns = [
    #path('list/', BoardListCreateView.as_view()),
    #path('', GoalViewSet.as_view()),
    path('', include(router.urls)),
]