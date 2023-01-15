from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter
from goal.models import Goal
from .serializers import GoalSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
