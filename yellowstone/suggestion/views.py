from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.

from suggestion.models import SuggestionCategory
from suggestion.model_serializer import SuggestionCategorySerializer


@api_view(['GET'])
@parser_classes((JSONParser,))
def suggestion_types(request):
    suggestions = SuggestionCategory.objects.all()
    serializer = SuggestionCategorySerializer(suggestions,many=True)
    return Response(serializer.data, status=200)