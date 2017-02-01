__author__ = 'parthverma'

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from mongoengine import *
from yellowstone.complaints.models import Complaint_Types
import datetime



class Complaint(Document):
    phone_regex = RegexValidator(regex=r'^\+?9?1?([7-9]|1)?\d{9}$', message="Invalid phone number")
    phone_number = models.CharField(validators=[phone_regex], blank=True)

    user_name = StringField(max_length = 50)
    user_id = IntField()
    is_anon = BooleanField(required=True)
    complaint_type = models.ForeignKey(
        'Complaint_Types', null=False, blank=False, on_delete=models.CASCADE, related_name='wishlist_users', requires = True)
    complaint_text = models.CharField(max_length=1000, required=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.complaint_category