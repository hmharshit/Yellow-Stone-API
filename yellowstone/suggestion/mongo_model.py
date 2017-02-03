__author__ = 'parthverma'

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from mongoengine import *
from yellowstone.suggestion.models import Suggestion_Sub_Category
import datetime



class Suggestion(Document):
    user_id = IntField()
    is_anon = BooleanField(required=True)
    complaint_type = models.ForeignKey(
        'Suggestion_Sub_Category', null=False, blank=False, on_delete=models.CASCADE, related_name='suggestion-category', requires = True)
    suggestion_text = models.CharField(max_length=1000, required=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.complaint_category
