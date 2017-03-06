__author__ = 'parthverma'

from rest_framework import serializers
from states.models import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        exclude = ('created_at', 'updated_at')