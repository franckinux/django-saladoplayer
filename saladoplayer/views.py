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

    #default parameter value does not work as expected !
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

        #get title, pan, tilt and url of each photo in the gallery
        photo_list = []
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
                photo_dict = {'photo': photo,
                              'title': photo.caption if photo.caption 
                                                     else photo_attrs[0],
                              'pan': pan,
                              'tilt': tilt,
                              'url': url
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

    #default parameter value does not work as expected !
    if hotspot is None:
        hotspot = 'hs'

    tour = get_object_or_404(Tour, title_slug=tour_slug)

    return render(request,
                  'saladoplayer/page.html',
                  {'tour': tour,
                   'tour_slug': tour_slug,
                   'hotspot': hotspot })
