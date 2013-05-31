#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.views
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from collections import defaultdict
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from saladoplayer.models import Tour

def get_photo_url(tour, photo):
    #get the filename of the photo in the requested size
    try:
        if tour.photo_size:
            size_method_str = 'get_%s_url' % tour.photo_size
            size_method = getattr(photo, size_method_str)
            url = size_method()
        else:
            #get the default filename if no size is available
            url = photo.image.name
    except:
        #get the default filename if something goes wrong
        url = photo.image.name
    return url

def xml(request, tour_slug, hotspot):
    """Renders the xml file needed by saladoplayer flash script"""

    #default parameter value does not work as expected !
    if hotspot is None:
        hotspot = 'hs'

    tour = get_object_or_404(Tour, title_slug=tour_slug)

    # default values
    panoramas = []

    # we iterate on all panoramas in the tour
    for panorama in tour.panorama_set.all():
        # consider all the panorama targets from the current panorama
        chainings = panorama.from_pano.all()

        # consider all information hotspots in the current panorama
        informations = panorama.informationhotspot_set.all()

        # consider all links in the current panorama
        links = panorama.linkhotspot_set.all()

        galleries = []
        # consider all the panorama galleries from the current panorama
        for gallery in panorama.galleryhotspot_set.all():
            photos = []
            for photo in gallery.gallery.photos.all():
                if not photo.is_public:
                    #photo is not public, skip photo
                    continue

                photos.append({'photo': photo,
                               'url': get_photo_url(tour, photo),
                              })

            galleries.append({'gallery': gallery,
                              'photos': photos,
                             })

        #get title, pan, tilt and url of each photo in the gallery
        photos = []
        if settings.MEDIA_URL and panorama.gallery:
            for photo in panorama.gallery.photos.all():
                if not photo.is_public:
                    #photo is not public, skip photo
                    continue

                #the title field value in the photo table must follow
                #this format : "title|pan|tilt"in order to be displayed
                photo_attrs = photo.title.split('|')
                if len(photo_attrs) != 3:
                    #wrong parameter format, skip photo
                    continue
                try:
                    pan = float(photo_attrs[1])
                    tilt = float(photo_attrs[2])
                except:
                    #wrong float format, skip photo
                    continue

                photos.append({'photo': photo,
                               'title': photo.caption if photo.caption
                                                      else photo_attrs[0],
                               'pan': pan,
                               'tilt': tilt,
                               'url': get_photo_url(tour, photo),
                              })

        panoramas.append({'panorama': panorama,
                          'chainings': chainings,
                          'informations': informations,
                          'links': links,
                          'photos': photos,
                          'galleries': galleries,
                         })

    # consider all maps in the current tour
    mappings = []
    for map in tour.map_set.all():
        mappings.append({'map': map,
                         'panorama_mappings': map.panoramamapping_set.all(),
                        })

    return render(request,
                  'saladoplayer/config.xml',
                  {'tour': tour,
                   'panoramas': panoramas,
                   'mappings': mappings,
                   'hotspot': hotspot == 'hs',
                  })

def html(request, tour_slug, hotspot):
    """Renders the template for standalone tour viewing"""

    #default parameter value does not work as expected !
    if hotspot is None:
        hotspot = 'hs'

    tour = get_object_or_404(Tour, title_slug=tour_slug)

    return render(request,
                  'saladoplayer/page.html',
                  {'tour': tour,
                   'tour_slug': tour_slug,
                   'hotspot': hotspot })
