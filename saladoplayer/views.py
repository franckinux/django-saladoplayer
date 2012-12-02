#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.views
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.shortcuts import render, get_object_or_404
from saladoplayer.models import Tour

def xml(request, tour_slug, hotspot):
    """Renders the xml file needed by saladoplayer flash script."""
    if hotspot is None:
        hotspot = 'hs'

    tour = get_object_or_404(Tour, title_slug=tour_slug)

    # default values
    panorama_list = []

    # we iterate on all panoramas in the tour
    panoramas = tour.panorama_set.all()

    for panorama in panoramas:
        # consider all the targets from the current panorama
        chaining_list = panorama.from_pano.all()

        # consider each information from the current panorama
        information_list = panorama.hotspotinformation_set.all()

        panorama_list.append({'panorama': panorama,
                              'chaining_list': chaining_list,
                              'information_list': information_list,
                             })

    return render(request,
                  'saladoplayer/config.xml',
                  {'tour': tour,
                   'panorama_list': panorama_list,
                   'hotspot': hotspot == 'hs',
                  })

def html(request, tour_slug, hotspot):

    if hotspot is None:
        hotspot = 'hs'

    tour = get_object_or_404(Tour, title_slug=tour_slug)

    return render(request,
                  'saladoplayer/page.html',
                  {'tour': tour,
                   'tour_slug': tour_slug,
                   'hotspot': hotspot })
