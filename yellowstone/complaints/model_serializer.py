__author__ = 'parthverma'

from rest_framework import serializers
from yellowstone.complaints.models import Complaint_Category, Complaint_Sub_Category


class ComplaintCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint_Category
        fields = '__all__'


class ComplaintSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint_Sub_Category
        fields = '__all__'