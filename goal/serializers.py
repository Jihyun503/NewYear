from rest_framework import serializers
from .models import Goal


class GoalSerializer(serializers.ModelSerializer):
    #user = serializers.StringRelatedField() #PK값이 아닌 __str__ 메소드에서 정의한 string 을 가져오고 싶을때
    user = serializers.ReadOnlyField(source='user.email')
    percent = serializers.ReadOnlyField()

    class Meta:
        model = Goal
        fields = '__all__'
