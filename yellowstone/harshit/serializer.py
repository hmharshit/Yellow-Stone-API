__author__ = 'parthverma'
from rest_framework import serializers

from harshit.models import test

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = test
        fields='__all__'