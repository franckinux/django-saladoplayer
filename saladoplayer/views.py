#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.views
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.shortcuts import render, get_object_or_404
from saladoplayer.models import Tour, Chaining

def xml(request, tour_id, hotspot):
    """Renders the xml file needed by saladoplayer flash script."""
    tour = get_object_or_404(Tour, pk=tour_id)

    # default values
    panorama_list = []

    # we iterate on all panoramas in the tour
    panoramas = tour.panorama_set.all()

    for panorama in panoramas:
        targets = panorama.panorama_set.all()
        target_list = []

        # consider each target from the current panorama
        for target in targets:
            # get extra informations about the link between the panos
            chaining = Chaining.objects.get(from_panorama=panorama,
                                            to_panorama=target)

            target_list.append({'id': target.id,
                                'chaining': chaining,
                               })

        # consider each information from the current panorama
        information_list = panorama.hotspotinformation_set.all()

        panorama_config = {'panorama': panorama,
                           'target_list': target_list,
                           'information_list': information_list,
                          }
        panorama_list.append(panorama_config)

    return render(request,
                  'saladoplayer/config.xml',
                  {'tour': tour,
                   'panorama_list': panorama_list,
                   'hotspot': hotspot == 'hs',
                  })

