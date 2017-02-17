__author__ = 'parthverma'

from django.conf.urls import url, include

import suggestion.views

urlpatterns = [
    url(r'^categories/$', suggestion.views.suggestion_types, name='suggestion.suggestion_types'),
    url(r'^subcategories/$', suggestion.views.suggestion_sub_types, name='suggestion.suggestion_sub_types'),
    url(r'^suggestions/$', suggestion.views.suggestions, name='suggestion.suggestions')
]