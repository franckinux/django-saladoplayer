#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.views
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from saladoplayer.models import Tour

def xml(request, tour_slug, hotspot):
    """Renders the xml file needed by saladoplayer flash script"""

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

        #get title, pan, tilt of each photo in the gallery
        photo_list = []
        if settings.MEDIA_URL and panorama.photo_gallery:
            for photo in panorama.photo_gallery.photos.all():
                if photo.is_public:
                    #the title field value in the photo table must follow
                    #this format : "title|pan|tilt"in order to be displayed
                    photo_elements = photo.title.split('|')
                    if len(photo_elements) != 3:
                        continue
                    try:
                        pan = float(photo_elements[1])
                        tilt = float(photo_elements[2])
                    except:
                        #wrong float format !
                        continue
                    photo_dict = {'photo': photo,
                                  'title': photo_elements[0],
                                  'pan': pan,
                                  'tilt': tilt,
                                  'url': settings.MEDIA_URL + photo.image.name
                                 }
                    photo_list.append(photo_dict)

        else:
            photo_list = []

        panorama_list.append({'panorama': panorama,
                              'chaining_list': chaining_list,
                              'information_list': information_list,
                              'photo_list': photo_list,
                             })

    return render(request,
                  'saladoplayer/config.xml',
                  {'tour': tour,
                   'panorama_list': panorama_list,
                   'hotspot': hotspot == 'hs',
                  })

def html(request, tour_slug, hotspot):
    """Renders the template for standalone tour viewing"""

    if hotspot is None:
        hotspot = 'hs'

    return render(request,
                  'saladoplayer/page.html',
                  { 'tour_slug': tour_slug,
                    'hotspot': hotspot })
