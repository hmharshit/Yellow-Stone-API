__author__ = 'parthverma'

from rest_framework import serializers
from yellowstone.user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
