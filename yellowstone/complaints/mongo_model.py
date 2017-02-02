__author__ = 'parthverma'

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from mongoengine import *
from yellowstone.complaints.models import Complaint_Types
import datetime

from yellowstone.complaints.constants import *

class Complaint(Document):
    phone_regex = RegexValidator(regex=r'^\+?9?1?([7-9]|1)?\d{9}$', message="Invalid phone number")
    phone_number = CharField(validators=[phone_regex], blank=True)

    user_name = StringField(max_length = 50)
    user_id = IntField()
    is_anon = BooleanField(required=True)
    category_id = IntField(required=True)
    sub_category_id = InField(required=True)
    complaint_id = CharField(required=True)
    # complaint_type = models.ForeignKey(
    #     'Complaint_Types', null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_users', requires = True)
    complaint_text = CharField(max_length=1000, required=True)
    incident_on = DateTimeField()
    created_at = DateTimeField(auto_now_add=True)
    updated_on = DateTimeField(auto_now=True)
    priority_level = IntField(choices=LEVELS)
    status = StringField(choices=STATUS)

    def __str__(self):
        return self.complaint_category
