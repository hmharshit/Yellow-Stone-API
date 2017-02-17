__author__ = 'parthverma'

from rest_framework_mongoengine.serializers import DocumentSerializer

from complaints.mongo_model import Complaint


class ComplaintSerializer(DocumentSerializer):

    class Meta:
        model = Complaint
        fields = '__all__'

