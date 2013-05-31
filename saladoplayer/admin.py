#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.admin
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from saladoplayer.models import *

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class PanoramaInline(admin.TabularInline):
    model = Panorama
    extra = 2

class PanoramaAdminForm(forms.ModelForm):
    class Meta:
        model = Panorama

    def clean(self):
        cleaned_data = super(PanoramaAdminForm, self).clean()
        #check initial tilt
        initial_tilt = cleaned_data.get("initial_tilt")
        min_tilt = cleaned_data.get("min_tilt")
        max_tilt = cleaned_data.get("max_tilt")
        if initial_tilt:
            if min_tilt:
                if min_tilt > initial_tilt:
                    raise forms.ValidationError("Initial tilt must be greater than min_tilt")
            if max_tilt:
                if  max_tilt < initial_tilt:
                    raise forms.ValidationError("Initial tilt must be lower than max_tilt")
        #check points in map
        map = cleaned_data.get("map")
        x = cleaned_data.get("x")
        y = cleaned_data.get("y")
        if map:
            if not x or not y:
                raise forms.ValidationError("Missing x or y")
        return cleaned_data

class PanoramaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields': ['tour', 'directory', 'title', 'direction']}),
        ('Initial position', {'fields': [('initial_pan', 'initial_tilt')]}),
        ('Vertical field of view limitation', {'fields': [('min_tilt', 'max_tilt')]}),
        ('Photo gallery', {'fields': ['photo_gallery']}),
    ]
    form = PanoramaAdminForm

class TourAdminForm(forms.ModelForm):
    class Meta:
        model = Tour

    def clean(self):
        cleaned_data = super(TourAdminForm, self).clean()
        #check facebook parameters
        facebook = cleaned_data.get("facebook")
        description = cleaned_data.get("description")
        thumb = cleaned_data.get("thumb")
        if facebook and not (description and thumb):
            raise forms.ValidationError("A description and a thumb image are needed to be included in Facebook metadata")
        #check gallery parameters
        scrollmenu = cleaned_data.get("scrollmenu")
        photo_size = cleaned_data.get("photo_size")
        if not photo_size:
            raise forms.ValidationError('You must define and use a photologue size')
        return cleaned_data


class TourAdmin(admin.ModelAdmin):
    inlines = [PanoramaInline]
    fieldsets = [
        ('', {'fields': [('title', 'title_slug', 'first_panorama')]}),
        ('Tour options', {'fields': [('dropmenu', 'auto_rotation', 'zoomslider', 'viewfinder', 'full_screener', 'compass')]}),
        ('Photos galleries', {'fields': ['scrollmenu', 'photo_size']}),
        ('Nadir hotspot', {'fields': ['nadir']}),
        ('FaceBook metadata', {'fields': ['facebook', 'description', 'thumb', ('height', 'width')]}),
    ]
    prepopulated_fields = {'title_slug': ('title',)}
    form = TourAdminForm

class PanoramaHotspotAdminForm(forms.ModelForm):
    class Meta:
        model = PanoramaHotspot

    def clean(self):
        cleaned_data = super(PanoramaHotspotAdminForm, self).clean()
        from_panorama = cleaned_data.get('from_panorama')
        to_panorama = cleaned_data.get('to_panorama')
        if from_panorama.id == to_panorama.id:
            raise forms.ValidationError('Source and destination panoramas must be distinct')
        if from_panorama.tour.id != to_panorama.tour.id:
            raise forms.ValidationError('Source and destination panoramas must belong to the same tour')
        return cleaned_data

class PanoramaMappingInlineFormSet(forms.models.BaseInlineFormSet):
    def clean(self):
        super(PanoramaMappingInlineFormSet, self).clean()
        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data:
                cleaned_data = form.cleaned_data
                map = cleaned_data.get('map')
                pano = cleaned_data.get('panorama')
                if pano.tour.id != map.tour.id:
                    raise forms.ValidationError('The panorama does not belong to the image map belongs to')
        return

class PanoramaMappingInline(admin.TabularInline):
    model = PanoramaMapping
    extra = 2
    formset = PanoramaMappingInlineFormSet

class PanoramaMappingAdminForm(forms.ModelForm):
    class Meta:
        model = PanoramaMapping

    def clean(self):
        cleaned_data = super(PanoramaMappingAdminForm, self).clean()
        #check point position in the image map
        map = cleaned_data.get('map')
        x = cleaned_data.get('x')
        y = cleaned_data.get('y')
        if x > map.map_image.image.width or y > map.map_image.image.height:
            raise forms.ValidationError('Point outside the map')
        #check that the pano is in the tour
        pano = cleaned_data.get('panorama')
        if pano.tour.id != map.tour.id:
            raise forms.ValidationError('The panorama does not belong to the image map belongs to')
        return cleaned_data

class PanoramaMappingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields': ['map', 'panorama']}),
        ('Position', {'fields': [('x', 'y')]}),
    ]
    form = PanoramaMappingAdminForm

class MapAdminForm(forms.ModelForm):
    class Meta:
        model = Map

class MapAdmin(admin.ModelAdmin):
    inlines = [PanoramaMappingInline]
    fieldsets = [
        ('', {'fields': ['map_image', 'tour', 'pan_shift']}),
    ]
    form = MapAdminForm

class PanoramaHotspotAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Panorama chaining', {'fields': ['from_panorama', 'to_panorama']}),
        ('Position', {'fields': [('pan', 'tilt')]}),
        ('Options', {'fields': ['show_information']}),
    ]
    form = PanoramaHotspotAdminForm

class InformationHotspotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['panorama', 'title']}),
        ('Position', {'fields': [('pan', 'tilt')]}),
    ]

class LinkHotspotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['panorama', 'url', 'title']}),
        ('Position', {'fields': [('pan', 'tilt')]}),
    ]

class GalleryHotspotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['panorama']}),
        ('Position', {'fields': [('pan', 'tilt')]}),
        ('Photo gallery', {'fields': ['gallery']}),
    ]

admin.site.register(Tour, TourAdmin)
admin.site.register(Panorama, PanoramaAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(PanoramaMapping, PanoramaMappingAdmin)
admin.site.register(PanoramaHotspot, PanoramaHotspotAdmin)
admin.site.register(InformationHotspot, InformationHotspotAdmin)
admin.site.register(LinkHotspot, LinkHotspotAdmin)
admin.site.register(GalleryHotspot, GalleryHotspotAdmin)
