__author__ = 'parthverma'

from rest_framework import serializers
from yellowstone.suggestion.models import Suggestion_Category, Suggestion_Sub_Category


class SuggestionCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Suggestion_Category
        fields = '__all__'


class Suggestion_Sub_Category(serializers.ModelSerializer):

    class Meta:
        model = Suggestion_Sub_Category
        fields = '__all__'



