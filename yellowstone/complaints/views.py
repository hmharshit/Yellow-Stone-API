from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from complaints.models import ComplaintCategory, ComplaintSubCategory
from complaints.model_serializer import ComplaintCategorySerializer, ComplaintSubCategorySerializer
# Create your views here.


@api_view(['GET'])
@parser_classes((JSONParser,))
def complaint_types(request):
    Types = ComplaintCategory.objects.all()
    serializer = ComplaintCategorySerializer(Types, many=True)
    return Response(data=serializer.data,status=200)


@api_view(['GET'])
@parser_classes((JSONParser,))
def complaint_sub_types(request):
    category = request.query_params.get('category',None)
    if category is None:
        subcats = ComplaintSubCategory.objects.all()
        subcats_serializer = ComplaintSubCategorySerializer(subcats,many=True)
        content=[]
        for cats in subcats_serializer.data:
            content.append(subcats_serializer.data)
            cat_id = cats.pop('complaint_category')
            cat = ComplaintCategory.objects.get(id=cat_id)
            cat_data =ComplaintCategorySerializer(cat)
            cats['category'] = cat_data.data

        return Response(data=subcats_serializer.data,status=200)
    else:
        try:
            cat = ComplaintCategory.objects.get(name = category)
        except:
            return Response(data=[],status=404)
        cat_data = ComplaintCategorySerializer(cat).data
        print(cat_data)
        cat_id = cat_data['id']
        try:
            sub_cat = ComplaintSubCategory.objects.filter(complaint_category_id= cat_id)
        except:
            return Response(data=[],status=404)

        sub_cat_data = ComplaintSubCategorySerializer(sub_cat,many=True).data

        return Response(data=sub_cat_data,status=200)