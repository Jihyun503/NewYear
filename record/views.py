from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from .models import Record
from goal.models import Goal
from .serializers import RecordSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Max


class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    
    def list(self, request):
        records = self.queryset.filter(user=request.user)
        serializer = RecordSerializer(records, many=True)

        return Response(serializer.data)
     
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        goal = Goal.objects.get(bno=request.data.get("goal"))
        if goal.percent < int(request.data.get("percent")):  # 퍼센트가 줄지 않고 상승만 한다는 전제 하에
            goal.percent = request.data.get("percent")

        goal.save()

        return Response(request.data)
    
    def update(self, request, pk):
        instance = get_object_or_404(self.queryset, id=pk)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        goal = Goal.objects.get(bno=request.data.get("goal"))
        if goal.percent < int(request.data.get("percent")):
            goal.percent = request.data.get("percent")
            
        goal.save()

        return Response(request.data)

    def delete(self, request, pk):
        print("들어왓다고;;")
        instance = get_object_or_404(self.queryset, id=pk)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("들어옴")
        try:
            qs = Record.objects.all(goal=request.data.get("goal"))
        except Exception:
            goal = Goal.objects.get(bno=request.data.get("goal"))
            goal.percent = 0
            goal.save()
        
        obj = Record.objects.aggregate(percent_max=Max('percent'))
        print(obj)

        goal = Goal.objects.get(bno=request.data.get("goal"))
        goal.percent = obj['percent_max']
        goal.save()

        return Response(request.data)

