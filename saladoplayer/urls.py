#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.urls
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^xml/(?P<tour_slug>[\w-]+)/((?P<hotspot>(no)?hs)/)?$', 'saladoplayer.views.xml'),
    url(r'^html/(?P<tour_slug>[\w-]+)/((?P<hotspot>(no)?hs)/)?$', 'saladoplayer.views.html'),
)

#references
#http://thefekete.net/blog/slug-urlconf-regex-pattern-for-django-urlpatterns/
#http://www.regular-expressions.info/optional.html