from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from complaints.models import ComplaintCategory
from complaints.model_serializer import ComplaintCategorySerializer
# Create your views here.


@api_view(['GET'])
@parser_classes((JSONParser,))
def complaint_types(request):
    Types = ComplaintCategory.objects.all()
    serializer = ComplaintCategorySerializer(Types, many=True)
    return Response(data=serializer.data,status=200)
