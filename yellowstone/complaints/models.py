from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Complaint_Types(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(max_length=50,populate_from=name, unique=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('slug',)
        db_table = 'complaint_types'

    def __str__(self):
        return self.name