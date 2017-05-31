"""djagios URL Configuration

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
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from data_collector.views import RecordDataApiView

from data_collector.views import StatusView
from data_collector.views import AlertListView
from data_collector.views import NewAlertView
from data_collector.views import EditAlertView
from data_collector.views import DeleteAlertView


urlpatterns = [
    url(r'^$', StatusView.as_view(), name='status'),

    url(r'^alerts/$', AlertListView.as_view(), name='alerts-list'),
    url(r'^alerts/new/$', NewAlertView.as_view(), name='alerts-new'),
    url(r'^alerts/(?P<pk>\d+)/edit/$', EditAlertView.as_view(), name='alerts-edit'),
    url(r'^alerts/(?P<pk>\d+)/delete/$', DeleteAlertView.as_view(), name='alerts-delete'),
    url(r'^record/$', csrf_exempt(RecordDataApiView.as_view()), name='record-data'),

]
