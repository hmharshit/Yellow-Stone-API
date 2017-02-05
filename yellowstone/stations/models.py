from django.db import models
from autoslug import AutoSlugField
# Create your models here.


class Station(models.Model):
    station_code = models.CharField(max_length=10, null=False)
    latitude = models.DecimalField(max_digits=11, decimal_places=7)
    longitude = models.DecimalField(max_digits=11, decimal_places=7)
    name = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(max_length=100, populate_from=name, unique=True)
    state = models.CharField(max_length=30, null=False)
    city = models.CharField(max_length=30, null=False)
    area = models.CharField(max_length=20)

    class Meta:
        db_table = 'stations'