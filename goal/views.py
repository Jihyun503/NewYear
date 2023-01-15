from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from .models import Goal
from .serializers import GoalSerializer
from .permissions import IsOwnerOrReadOnly


class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
    #authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    
    def list(self, request):
        goals = self.queryset.filter(user=request.user)
        serializer = GoalSerializer(goals, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
