__author__ = 'parthverma'

from rest_framework import serializers

from stations.models import Stations

class StationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stations
        fields = '__all__'