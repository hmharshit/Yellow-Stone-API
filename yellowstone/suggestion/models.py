from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class SuggestionCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(max_length=50,populate_from='name', unique=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('slug',)
        db_table = 'suggestiontypes'

    def __str__(self):
        return self.name

class SuggestionSubCategory(models.Model):

    suggestion_category = models.ForeignKey(
        SuggestionCategory, null=False, blank=False, on_delete=models.CASCADE, related_name='xyz_comp')
    name = models.CharField(max_length=60)
    slug = AutoSlugField(max_length=60, populate_from='name', unique=True)

    class Meta:
        unique_together = ('suggestion_category', 'id')
        db_table = 'suggestion_subtypes'
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('slug',)

    def __str__(self):
        return self.name