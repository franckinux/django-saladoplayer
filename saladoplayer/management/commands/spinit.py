#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.admin
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.core.files import File

class Command(BaseCommand):
    help = 'Initialization is salasoplyer app'

    def handle(self, *args, **options):
        try:
            from photologue.models import Gallery, Photo, PhotoSize
        except:
            self.stderr.write('photologue is not installed. Install it fist.\n')
            return

        # check the thumnail size
        photo_size = PhotoSize.objects.filter(name__exact='thumbnail')
        if not photo_size:
            self.stderr.write('you have not defined the thumbnail size. run plinit and define it.\n')
            return

        # check the saladoplayer gallery
        hotspots = {'see': 'oeil_jaune_noir_rond.png',
                    'info':'info_bleu_blanc_triangle.png',
                    'goto': 'pas_orange_blanc_carre.png',
                    'link': 'fleche_bleu_blanc_rond.png',
                   }
        gallery = Gallery.objects.filter(title_slug__exact='saladoplayer')
        if gallery:
            self.stdout.write('saladoplayer gallery already exists\n')
            photos = Photo.objects.filter(galleries__exact=gallery)
            if len(photos) != len(hotspots):
                self.stderr.write('incorrect number of photos in the saladoplayer gallery\n')
            for photo in photos:
                if not photo.title_slug in hotspots.keys():
                    self.stderr.write('incorrect title of photo in the saladoplayer gallery\n')
                    self.stderr.write('invalid photo %s in saladoplayer gallery\n' % photo.title)
                    return
            return

        #create saladoplayer gallery
        creation_date = timezone.localtime(timezone.now())
        g = Gallery(title='saladoplayer', title_slug='saladoplayer',
                    description='for use by saladoplayer app',
                    date_added=creation_date)
        g.save()
        # create three default hotspots and add them to the gallery
        for k, v in hotspots.items():
            f = File(open("saladoplayer/static/hotspots/images/%s" % v))
            p = Photo(title=k, title_slug=k, image=f,
                      date_added=creation_date, date_taken=creation_date)
            p.save()
            f.close()
            g.photos.add(p)
        self.stdout.write('saladoplayer gallery successfuly added\n')