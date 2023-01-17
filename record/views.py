from rest_framework import viewsets
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .models import Record
from goal.models import Goal
from .serializers import RecordSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Max


class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset

    def list(self, request):
        records = self.queryset.filter(user=request.user)
        serializer = RecordSerializer(records, many=True)

        return Response(serializer.data)
     
    def create(self, request):
        goal = get_object_or_404(Goal.objects.filter(user=request.user, bno=request.data.get("goal")))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        if goal.percent < int(request.data.get("percent")):  # 퍼센트가 줄지 않고 상승만 한다는 전제 하에
            goal.percent = request.data.get("percent")

        goal.save()

        return Response(request.data)
    
    def update(self, request, pk):
        #instance = get_object_or_404(self.queryset, id=pk)
        instance = get_object_or_404(self.queryset.filter(user=request.user, id=pk))
        
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        goal = Goal.objects.get(bno=request.data.get("goal"))
        if goal.percent < int(request.data.get("percent")):
            goal.percent = request.data.get("percent")
            
        goal.save()

        return Response(request.data)

    def destroy(self, request, pk):
        instance = get_object_or_404(self.queryset, id=pk)
        stdgoal = instance.goal
        instance.delete()

        goal = Goal.objects.get(bno=stdgoal.bno)
        record = Record.objects.filter(goal=stdgoal)

        if record.exists() is False:
            goal.percent = 0
            goal.save()

            return Response(request.data)

        obj = record.aggregate(percent_max=Max('percent'))

        goal.percent = obj['percent_max']
        goal.save()

        return Response(request.data)
