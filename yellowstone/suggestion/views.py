from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.

from suggestion.models import SuggestionCategory, SuggestionSubCategory
from suggestion.model_serializer import SuggestionCategorySerializer, SuggestionSubCategorySerializer
from suggestion.mongo_serializer import SuggestionSerializer
from suggestion.mongo_model import Suggestion


@api_view(['GET'])
@parser_classes((JSONParser,))
def suggestion_types(request):
    suggestions = SuggestionCategory.objects.all()
    serializer = SuggestionCategorySerializer(suggestions,many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
@parser_classes((JSONParser,))
def suggestion_sub_types(request):
    category = request.query_params.get('category',None)
    if category is None:
        subcats = SuggestionSubCategory.objects.all()
        subcats_serializer = SuggestionSubCategorySerializer(subcats,many=True)
        content=[]
        for cats in subcats_serializer.data:
            content.append(subcats_serializer.data)
            cat_id = cats.pop('complaint_category')
            cat = SuggestionCategory.objects.get(id=cat_id)
            cat_data =SuggestionCategorySerializer(cat)
            cats['category'] = cat_data.data

        return Response(data=subcats_serializer.data,status=200)
    else:
        try:
            cat = SuggestionCategory.objects.get(name = category)
        except:
            return Response(data=[],status=404)
        cat_data = SuggestionCategorySerializer(cat).data
        print(cat_data)
        cat_id = cat_data['id']
        try:
            sub_cat = SuggestionSubCategory.objects.filter(suggestion_category_id= cat_id)
        except:
            return Response(data=[],status=404)

        sub_cat_data = SuggestionSubCategorySerializer(sub_cat,many=True).data

        return Response(data=sub_cat_data,status=200)

@api_view(['GET', 'POST'])
@parser_classes((JSONParser,))
def suggestions(request):
    if request.method == 'GET':
        suggestion = Suggestion.objects.all()
        serializer = SuggestionSerializer(suggestion, many=True)
        return Response(data=serializer.data, status=200)
    else:
        suggestion = SuggestionSerializer(data=request.data)
        if suggestion.is_valid():
            suggestion.save()
            return Response(data=suggestion.data, status=200)
        else:
            return Response(data=suggestion.errors, status=400)