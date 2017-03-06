from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=15)
    slug = AutoSlugField(populate_from='name', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('slug',)
        db_table = 'states'