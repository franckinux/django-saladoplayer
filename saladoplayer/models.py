#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.model
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify

class AngleDecimalField(models.DecimalField):
    """Class defining an angular position. It serves as a base class
    for both PanDecimalField and TiltDecimalField"""
    def __init__(self, optional, angle, *args, **kwargs):
        kwargs['max_digits'] = 6
        kwargs['decimal_places'] = 2
        kwargs['validators'] = [MinValueValidator(-angle), MaxValueValidator(angle)]
        if optional:
            kwargs['blank'] = True
            kwargs['null'] = True
        super(AngleDecimalField, self).__init__(*args, **kwargs)

class PanDecimalField(AngleDecimalField):
    """Class defining the pan angular position"""
    def __init__(self, optional=False, *args, **kwargs):
        super(PanDecimalField, self).__init__(optional, angle=180, *args, **kwargs)

class TiltDecimalField(AngleDecimalField):
    """Class defining the tilt angular position"""
    def __init__(self, optional=False, *args, **kwargs):
        super(TiltDecimalField, self).__init__(optional, angle=90, *args, **kwargs)

class Tour(models.Model):
    """Defines the panoramas in the tour."""
    title = models.CharField(max_length=64, unique=True)
    title_slug = models.SlugField(max_length=64, unique=True,
          help_text=('A "slug" is a unique URL-friendly title for an object.'))
    display_dropmenu = models.BooleanField()
    display_viewfinder = models.BooleanField()
    auto_rotation = models.BooleanField()
    facebook = models.BooleanField()
    description = models.TextField(blank=True)
    thumb = models.CharField(max_length=128, blank=True)
    #related name is needed otherwise it chashes with tour field of Panorama
    first_panorama = models.ForeignKey('Panorama', 
                                       blank=True, null=True,
                                       related_name='first_panorama')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title_slug is None:
            self.title_slug = slugify(self.title)
        return super(Tour, self).save(*args, **kwargs)
 
class Panorama(models.Model):
    """Defines the panorama : what tour it belongs to, in what directory
    it lies, how to move to other panoramas and what is the initial
    position of the camera."""
    tour = models.ForeignKey('Tour')
    directory = models.CharField(max_length=128)
    information = models.CharField(max_length=128)
    chaining = models.ManyToManyField('self',
                                      through='Chaining',
                                      symmetrical=False)
    initial_pan = PanDecimalField(optional=True)
    initial_tilt = TiltDecimalField(optional=True)
    min_tilt = TiltDecimalField(optional=True)
    max_tilt = TiltDecimalField(optional=True)

    def __unicode__(self):
        return "%s / %s" % (self.tour.title, self.information)

class Chaining(models.Model):
    """Defines the link between two panoramas, the source and the destination.
    The show_description boolean decides whether the panorama information must
    be shown when the cursor is over the hotspot."""
    from_panorama = models.ForeignKey('Panorama', related_name='from_pano')
    to_panorama = models.ForeignKey('Panorama', related_name='to_pano')
    show_information = models.BooleanField()
    pan = PanDecimalField()
    tilt = TiltDecimalField()

    def __unicode__(self):
        return "%s / %s -> %s / %s" % (self.from_panorama.tour.title,
                                       self.from_panorama.information,
                                       self.to_panorama.tour.title,
                                       self.to_panorama.information)

    class Meta:
        unique_together = (('from_panorama', 'to_panorama'),)

class HotspotInformation(models.Model):
    """Defines the information that is displayed when the cursor is over
    the information hotspot."""
    panorama = models.ForeignKey('Panorama')
    information = models.CharField(max_length=128)
    pan = PanDecimalField()
    tilt = TiltDecimalField()

    def __unicode__(self):
        return "%s / %s / %s" % (self.panorama.tour.title, 
                                 self.panorama.information,
                                 self.information)
    
