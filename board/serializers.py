from rest_framework import serializers
from goal.models import Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('user', 'goal', 'contents')
