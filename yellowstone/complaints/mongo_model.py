__author__ = 'parthverma'

from django.db import models
from django.utils import timezone
from mongoengine import *
import datetime

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
CLEAN = 'Cl'
COMPLAINT_CATEGORIES = ((CLEAN, 'cleanliness'), (), (),)


class Complaint(Document):

    user_name = StringField(max_length = 50)
    user_id = IntField()
    isanon = BooleanField(required=True)
    complaint_category = models.CharField(max_length=200, choices=COMPLAINT_CATEGORIES)
    complaint_text = models.CharField(max_length=1000)
    pub_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.complaint_category

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()
