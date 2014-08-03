from django.conf.urls import include, patterns, url

from django.views.generic import ListView, DetailView

from models import *

activity_detail = DetailView.as_view(model=Activity)
dashboard = DetailView.as_view(model=Person)

urlpatterns = patterns('',
    url(r'^activity/$', activity_detail, name='activity_detail'),
    url(r'^$', dashboard, name='dashboard'),
)