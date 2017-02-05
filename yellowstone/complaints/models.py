from django.db.models import CharField, ForeignKey, Model, CASCADE
from autoslug import AutoSlugField


class ComplaintCategory(Model):
    name = CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete', 'view')
        ordering = ('slug',)
        db_table = 'complaint_types'

    def __str__(self):
        return self.name


class ComplaintSubCategory(Model):
    complaint_category = ForeignKey(
        ComplaintCategory, null=False, blank=False, on_delete=CASCADE, related_name='xyz_comp')
    name = CharField(max_length=60)
    slug = AutoSlugField(max_length=60, populate_from='name', unique=True)

    class Meta:
        db_table = 'complaint_sub_types'