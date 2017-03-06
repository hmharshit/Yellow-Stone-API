__author__ = 'parthverma'
from django.conf.urls import url, include

import states.views

urlpatterns = [
    url(r'$', states.views.statelist, name='states.states'),
]