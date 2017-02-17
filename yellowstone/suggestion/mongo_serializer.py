__author__ = 'parthverma'

from rest_framework_mongoengine.serializers import DocumentSerializer
from suggestion.mongo_model import Suggestion


class SuggestionSerializer(DocumentSerializer):

    class Meta:
        model = Suggestion
        fields = '__all__'
