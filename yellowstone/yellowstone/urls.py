"""yellowstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from complaints.urls import urlpatterns as complaint_urls
from suggestion.urls import urlpatterns as suggestion_urls
from stations.urls import urlpatterns as station_urls
from states.urls import urlpatterns as state_urls
from harshit.url import urlpatterns as test_urls

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^complaint/', include(complaint_urls)),
    url(r'^suggestion/',include(suggestion_urls)),
    url(r'^stations/', include(station_urls)),
    url(r'^state/',include(state_urls)),
    url(r'^test/',include(test_urls)),
]