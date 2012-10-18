#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.model
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class PanDecimalField(models.DecimalField):
    """Class defining the pan position"""
    def __init__(self, optional=False, *args, **kwargs):
        self.max_digits = 6
        self.decimal_places = 2
        self.validators = [MinValueValidator(-180), MaxValueValidator(180)]
        if optional:
            self.blank=True
            self.null=True
        super(PanDecimalField, self).__init__(*args, **kwargs)

class TiltDecimalField(models.DecimalField):
    """Class defining the pan position"""
    def __init__(self, optional=False, *args, **kwargs):
        self.max_digits = 6
        self.decimal_places = 2
        self.validators = [MinValueValidator(-90), MaxValueValidator(90)]
        if optional:
            self.blank=True
            self.null=True
        super(PanDecimalField, self).__init__(*args, **kwargs)

class Position(models.Model):
    """Meta class for defining a position in a panorama."""
    pan = models.DecimalField(max_digits=6, decimal_places=2,
                              validators = [MinValueValidator(-180),
                                            MaxValueValidator(180)])
    tilt = models.DecimalField(max_digits=6, decimal_places=2,
                              validators = [MinValueValidator(-90),
                                            MaxValueValidator(90)])
    
    class Meta:
        abstract = True
    
class Tour(models.Model):
    """Defines the panoramas in the tour."""
    title = models.CharField(max_length=64)
    display_dropmenu = models.BooleanField()

    def __unicode__(self):
        return self.title

class Panorama(models.Model):
    """Defines the panorama : what tour it belongs to, in what directory
    it lies, how to move to other panoramas and what is the initial
    position of the camera."""
    tour = models.ForeignKey(Tour)
    directory = models.CharField(max_length=64)
    information = models.CharField(max_length=128)
    chaining = models.ManyToManyField('self',
                                      through='Chaining',
                                      symmetrical=False)
    initial_pan = models.DecimalField(max_digits=6, decimal_places=2,
                              validators = [MinValueValidator(-180),
                                            MaxValueValidator(180)],
                                            blank=True,null=True)
    initial_tilt = models.DecimalField(max_digits=6, decimal_places=2,
                              validators = [MinValueValidator(-90),
                                            MaxValueValidator(90)],
                                            blank=True,null=True)
    min_tilt = models.DecimalField(max_digits=6, decimal_places=2,
                              validators = [MinValueValidator(-90),
                                            MaxValueValidator(90)],
                                            blank=True,null=True)
    max_tilt = models.DecimalField(max_digits=6, decimal_places=2,
                              validators = [MinValueValidator(-90),
                                            MaxValueValidator(90)],
                                            blank=True,null=True)

    def __unicode__(self):
        return "%s / %s" % (self.tour.title, self.information)

class InitialPanorama(models.Model):
    """Defines de initial paranamara of the tour."""
    tour = models.ForeignKey(Tour, unique=True)
    panorama = models.ForeignKey(Panorama)

class Chaining(Position):
    """Defines the link between two panoramas, the source and the destination.
    The show_description boolean decides whether the panorama information must
    be shown when the cursor os over the hotspot."""
    from_panorama = models.ForeignKey(Panorama, related_name='from_pano')
    to_panorama = models.ForeignKey(Panorama, related_name='to_pano')
    show_information = models.BooleanField()

    def __unicode__(self):
        return "%s / %s -> %s / %s" % (self.from_panorama.tour.title,
                                       self.from_panorama.information,
                                       self.to_panorama.tour.title,
                                       self.to_panorama.information)

    class Meta:
        unique_together = (('from_panorama', 'to_panorama'),)

class HotspotInformation(Position):
    """Defines the information that is displayed when the cursor is over
    the information hotspot."""
    panorama = models.ForeignKey(Panorama)
    information = models.CharField(max_length=128)

    def __unicode__(self):
        return "%s / %s" % (self.panorama.tour.title, self.information)
    
