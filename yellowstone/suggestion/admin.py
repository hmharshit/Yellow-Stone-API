from django.contrib import admin
from suggestion.models import SuggestionCategory,SuggestionSubCategory
# Register your models here.

admin.site.register(SuggestionCategory)
admin.site.register(SuggestionSubCategory)
