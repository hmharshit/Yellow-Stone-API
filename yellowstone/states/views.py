from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from states.models import State
from states.serializers import StateSerializer


@api_view(['GET'])
@parser_classes((JSONParser,))
def statelist(request):
    states = State.objects.all()
    serializer = StateSerializer(states, many=True)
    return Response(data=serializer.data, status=200)
