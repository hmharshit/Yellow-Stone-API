from django.db import models
from autoslug import AutoSlugField

class Complaint_Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(max_length=50, populate_from=name, unique=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('slug',)
        db_table = 'complaint_types'

    def __str__(self):
        return self.name

class Complaint_Sub_Category(models.Model):
    complaint_category = models.ForeignKey(
          Complaint_Category, null=False, blank=False, on_delete=models.CASCADE, related_name='xyz_comp')
    name = models.CharField(max_length=60)
    slug = AutoSlugField(max_length=60, populate_from=name, unique=True)

    class Meta:
        db_table = 'complaint_sub_types'