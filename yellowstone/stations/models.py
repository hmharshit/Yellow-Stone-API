from django.db import models
from autoslug import AutoSlugField
# Create your models here.


class Station(models.Model):
    station_id = models.IntegerField(null=False, unique=True)
    name = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(max_length=100, populate_from=name, unique=True)
    state = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)