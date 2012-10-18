#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.views
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.shortcuts import render, get_object_or_404
from saladoplayer.models import Tour, Chaining

def xml(request, tour_id, hotspot):
    """Renders the xml file needed by saladoplayer flash script"""
    tour = get_object_or_404(Tour, pk=tour_id)

    # initial panorama in the tour
    initial_panorama_list = tour.initialpanorama_set.all()
    initial_panorama = initial_panorama_list[0].panorama_id \
                       if len(initial_panorama_list) == 1 else None

    # default values
    panorama_list = []

    # we iterate on all panoramas in the tour
    panoramas = tour.panorama_set.all()

    for panorama in panoramas:
        targets = panorama.panorama_set.all()
        informations = panorama.hotspotinformation_set.all()

        # init defaults
        target_list = []
        information_list = []

        # consider each target from the current panorama
        for target in targets:
            # get extra informations about the link between the panos
            chaining = Chaining.objects.get(from_panorama=panorama,
                                            to_panorama=target)

            target_list.append({'pan': chaining.pan,
                                'tilt': chaining.tilt,
                                'id': target.id,
                                'show_information': chaining.show_information})

        # consider each information from the current panorama
        for information in informations:
            information_list.append({'pan': information.pan,
                                     'tilt': information.tilt,
                                     'id': information.id,
                                     'information': information.information})

        panorama_config = {'id': panorama.id,
                           'information': panorama.information,
                           'directory': panorama.directory,
                           'target_list': target_list,
                           'information_list': information_list,
                           'pan': panorama.initial_pan,
                           'tilt': panorama.initial_tilt,
                           'min_tilt': panorama.min_tilt,
                           'max_tilt': panorama.max_tilt,}
        panorama_list.append(panorama_config)

    return render(request,
                  'saladoplayer/config.xml',
                  {'tour': tour,
                   'panorama_list': panorama_list,
                   'initial_panorama': initial_panorama,
                   'hotspot': hotspot == 'hs' })

