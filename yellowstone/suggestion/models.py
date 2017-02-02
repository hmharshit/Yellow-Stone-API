from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Suggestion_Category(models.Model):
    category_id = models.IntegerField(unique = True, primary_key = True)
    name = models.CharField(max_length=50)
    slug = AutoSlugField(max_length=50,populate_from=name, unique=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('slug',)
        db_table = 'complaint_types'

    def __str__(self):
        return self.name

class Suggestion_Sub_Category(models.Model):
    sub_category_id = models.IntegerField()
    category_id = models.IntegerField()
    name = models.CharField(max_length=60)
    slug = AutoSlugField(max_length=60, populate_from=name, unique=True)

    class Meta:
        unique_together = ('category_id', 'sub_category_id')

    def __str__(self):
        return self.name