__author__ = 'parthverma'

from rest_framework import serializers

from stations.models import Station

class StationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = '__all__'