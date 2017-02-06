from django.contrib import admin
from complaints.models import ComplaintCategory,ComplaintSubCategory

# Register your models here.

admin.site.register(ComplaintCategory)
admin.site.register(ComplaintSubCategory)
