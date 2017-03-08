from django.db import models

# Create your models here.

class test(models.Model):
    name = models.CharField(max_length=20, null=False,blank=False)
    age = models.IntegerField(null=True, blank=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('name',)
        db_table = 'names'

c