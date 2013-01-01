#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.model
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.template.defaultfilters import slugify
from photologue.models import Gallery, Photo, PhotoSize

#this does not work on alwaysdata.com
#pan_kwargs = {'validators': [MinValueValidator(-180.0),
#                             MaxValueValidator(180.0)],
pan_kwargs = {'max_digits': 6,
              'decimal_places': 2,
             }
#this does not work on alwaysdata.com
#tilt_kwargs = {'validators': [MinValueValidator(-90.0),
#                              MaxValueValidator(90.0)],
tilt_kwargs = {'max_digits': 6,
               'decimal_places': 2,
              }

class Tour(models.Model):
    """Defines the panoramas in the tour."""
    title = models.CharField(max_length=64, unique=True)
    title_slug = models.SlugField(max_length=64, unique=True,
          help_text=('A "slug" is a unique URL-friendly title for an object'))
    dropmenu = models.BooleanField()
    viewfinder = models.BooleanField()
    scrollmenu = models.BooleanField()
    gallery = models.BooleanField(verbose_name=('Photo display interface'))
    zoomslider = models.BooleanField()
    auto_rotation = models.BooleanField()
    full_screener = models.BooleanField()
    compass = models.BooleanField()
    facebook = models.BooleanField()
    description = models.TextField(blank=True)
    thumb = models.ForeignKey(Photo,
                              blank=True, null=True,
                              related_name='thumb')
    height = models.IntegerField(default=600)
    width = models.IntegerField(default=800)
    first_panorama = models.ForeignKey('Panorama',
                                       blank=True, null=True,
                                       related_name='first_panorama')
    photo_size = models.ForeignKey(PhotoSize,
                                   blank=True, null=True)
    nadir = models.ForeignKey(Photo,
                              blank=True, null=True,
                              related_name='nadir')

    def save(self, *args, **kwargs):
        if self.title_slug is None:
            self.title_slug = slugify(self.title)
        return super(Tour, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Panorama(models.Model):
    """Defines the panorama : what tour it belongs to, in what directory
    it lies, how to move to other panoramas and what is the initial
    position of the camera."""
    tour = models.ForeignKey(Tour)
    directory = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    chaining = models.ManyToManyField('self',
                                      through='PanoramaHotspot',
                                      symmetrical=False)
    initial_pan = models.DecimalField(blank=True, null=True, **pan_kwargs)
    initial_tilt = models.DecimalField(blank=True, null=True, **tilt_kwargs)
    min_tilt = models.DecimalField(blank=True, null=True, **tilt_kwargs)
    max_tilt = models.DecimalField(blank=True, null=True, **tilt_kwargs)
    gallery = models.ForeignKey(Gallery,
                                blank=True, null=True)
    direction = models.DecimalField(blank=True, null=True, **pan_kwargs)

    def __unicode__(self):
        return "%s / %s" % (self.tour.title, self.title)

class PanoramaHotspot(models.Model):
    """Defines the link between two panoramas, the source and the destination.
    The show_description boolean decides whether the panorama information must
    be shown when the cursor is over the hotspot."""
    from_panorama = models.ForeignKey(Panorama, related_name='from_pano')
    to_panorama = models.ForeignKey(Panorama, related_name='to_pano')
    show_information = models.BooleanField()
    pan = models.DecimalField(**pan_kwargs)
    tilt = models.DecimalField(**tilt_kwargs)

    def __unicode__(self):
        return "%s / %s -> %s / %s" % (self.from_panorama.tour.title,
                                       self.from_panorama.title,
                                       self.to_panorama.tour.title,
                                       self.to_panorama.title)

    class Meta:
        unique_together = (('from_panorama', 'to_panorama'),)

class Map(models.Model):
    """Defines the image that will serve as a map in which panoramas are
    represented as hotspots. You can change of panorama by clicking on them.
    Direction and field of view of the currently displayed panorama are
    shown on the map."""
    map_image = models.ForeignKey(Photo)
    tour = models.ForeignKey(Tour)
    pan_shift = models.DecimalField(blank=True, null=True, **pan_kwargs)

    def __unicode__(self):
        return "%s / %s" % (self.map_image.title, self.tour.title)

class PanoramaMapping(models.Model):
    """Defines the position of the panorama in the image map."""
    map = models.ForeignKey(Map)
    panorama = models.ForeignKey(Panorama)
    x = models.IntegerField()
    y = models.IntegerField()

    def __unicode__(self):
        return "%s / %s" % (self.map.map_image.title,
                            self.panorama.title)

class InformationHotspot(models.Model):
    """Defines the information that is displayed when the cursor is over
    the information hotspot."""
    panorama = models.ForeignKey(Panorama)
    title = models.CharField(max_length=128)
    pan = models.DecimalField(**pan_kwargs)
    tilt = models.DecimalField(**tilt_kwargs)

    def __unicode__(self):
        return "%s / %s / %s" % (self.panorama.tour.title,
                                 self.panorama.title,
                                 self.title)

class LinkHotspot(models.Model):
    panorama = models.ForeignKey(Panorama)
    title = models.CharField(max_length=128)
    url = models.URLField()
    pan = models.DecimalField(**pan_kwargs)
    tilt = models.DecimalField(**tilt_kwargs)

    def __unicode__(self):
        return "%s / %s" % (self.panorama.title, self.title)

