__author__ = 'parthverma'
from django.conf.urls import url, include
import stations.views

urlpatterns = [
    url(r'$', stations.views.stations, name = 'stations.staions'),
]


