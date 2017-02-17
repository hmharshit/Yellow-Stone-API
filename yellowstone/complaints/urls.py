__author__ = 'parthverma'
from django.conf.urls import url, include
import complaints.views

urlpatterns = [
    url(r'^categories/$', complaints.views.complaint_types, name='complaints.complaint_types'),
    url(r'^subcats/$', complaints.views.complaint_sub_types, name='complaints.complaint_sub_types'),
    url(r'^complaints/$', complaints.views.complaints, name = 'complaints.complaints')]