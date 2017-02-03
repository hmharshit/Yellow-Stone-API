__author__ = 'parthverma'

from rest_framework_mongoengine.serializers import DocumentSerializer


class ComplaintMongoSerializer(DocumentSerializer):

    class Meta:
        model = Complaint

