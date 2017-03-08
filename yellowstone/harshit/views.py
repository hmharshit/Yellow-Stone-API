from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from harshit.models import test as a
from harshit.serializer import TestSerializer

@api_view(['GET'])
@parser_classes((JSONParser,))
def test(request):
    if request.method =='GET':
        tests = a.objects.all()
        serializer = TestSerializer(tests,many=True)
        return Response(data=serializer.data, status=200)