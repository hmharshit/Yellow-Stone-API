__author__ = 'parthverma'
from django.conf.urls import url, include
import complaints.views

urlpatterns = [
    url(r'^categories/$', complaints.views.complaint_types, name='complaints.complaint_types')]