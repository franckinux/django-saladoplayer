#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.urls
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^xml/(?P<tour_id>\d+)/(?P<hotspot>(no)?hs)/$', 'saladoplayer.views.xml'),
    url(r'^html/(?P<tour_id>\d+)/(?P<hotspot>(no)?hs)/$', 'saladoplayer.views.html'),
)
