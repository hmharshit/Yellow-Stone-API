__author__ = 'parthverma'

from django.conf.urls import url, include

import suggestion.views

urlpatterns = [
    url(r'^categories/$', suggestion.views.suggestion_types, name='suggestion.suggestion_types')
]