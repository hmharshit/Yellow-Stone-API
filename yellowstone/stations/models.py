from django.db import models
from autoslug import AutoSlugField
# Create your models here.


class Station(models.Models):
    station_id = models.IntField(required=True, unique=True)
    name = models.CharField(max_length=100, required =True)
    slug = AutoSlugField(max_length=100, populate_from=name,unique=True)
    state = models.CharField(max_length=30, required=True)
    city = models.CharField(max_length=30, required=True)