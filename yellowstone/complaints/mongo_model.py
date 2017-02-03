__author__ = 'parthverma'

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from mongoengine import *
from yellowstone.complaints.models import Complaint_Sub_Category, Complaint_Category
from yellowstone.user.models import User

from yellowstone.complaints.constants import *


class Complaint(Document):

    user = models.ForeignKey(User, on_delete=models.CASCADE, max_length=50)
    is_anon = BooleanField(required=True)

    complaint_category = models.ForeignKey(
        Complaint_Category, null=False, blank=False, on_delete=models.CASCADE, related_name='comp_type')

    complaint_sub_category = models.ForeignKey(Complaint_Sub_Category, on_delete=models.CASCADE)
    complaint_text = StringField(max_length=1000, required=True)
    incident_on = DateTimeField()
    created_at = DateTimeField(auto_now_add=True)
    updated_on = DateTimeField(auto_now=True)
    priority_level = IntField(choices=LEVELS)
    status = StringField(choices=STATUS)

    def __str__(self):
        return self.complaint_category
