from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from stations.models import Station
from stations.model_serializer import StationsSerializer

# Create your views here.

@api_view(['GET'])
@parser_classes((JSONParser,))
def stations(request):
    stations = Station.objects.all()
    station_serializer = StationsSerializer(stations,many =True)
    return Response(data = station_serializer.data, status=200)



