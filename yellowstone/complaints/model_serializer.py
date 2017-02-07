__author__ = 'parthverma'

from rest_framework import serializers
from complaints.models import ComplaintCategory, ComplaintSubCategory


class ComplaintCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ComplaintCategory
        fields = '__all__'


class ComplaintSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ComplaintSubCategory
        fields = '__all__'