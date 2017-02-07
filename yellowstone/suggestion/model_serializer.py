__author__ = 'parthverma'

from rest_framework import serializers
from suggestion.models import SuggestionCategory, SuggestionSubCategory


class SuggestionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SuggestionCategory
        fields = '__all__'


class SuggestionSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SuggestionSubCategory
        fields = '__all__'



