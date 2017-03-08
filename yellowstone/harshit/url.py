__author__ = 'parthverma'

from django.conf.urls import url, include

import harshit.views

urlpatterns = [
    url(r'$', harshit.views.test, name='states.states'),
]
