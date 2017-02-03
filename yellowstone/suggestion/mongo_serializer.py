__author__ = 'parthverma'

from rest_framework_mongoengine.serializers import DocumentSerializer


class SuggestionMongoSerializer(DocumentSerializer):

    class Meta:
        model = Complaint
