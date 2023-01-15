from rest_framework import serializers
from .models import Record
from goal.models import Goal


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        exclude = ('user',)
