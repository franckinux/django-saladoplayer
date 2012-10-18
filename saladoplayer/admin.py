#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.admin
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.contrib import admin
from django import forms
from saladoplayer.models import Tour, Panorama, Chaining, InitialPanorama, HotspotInformation

class PanoramaInline(admin.TabularInline):
    model = Panorama
    extra = 2

class PanoramaAdminForm(forms.ModelForm):
    class Meta:
        model = Panorama

    def clean(self):
        cleaned_data = super(PanoramaAdminForm, self).clean()
        initial_tilt = cleaned_data.get("initial_tilt")
        min_tilt = cleaned_data.get("min_tilt")
        max_tilt = cleaned_data.get("max_tilt")
        if initial_tilt:
          if min_tilt:
              if min_tilt > initial_tilt:
                  raise forms.ValidationError("initial tilt must be greater than min_tilt")
          if max_tilt:           
              if  max_tilt < initial_tilt:
                  raise forms.ValidationError("initial tilt must be lower than max_tilt")
        return cleaned_data

class PanoramaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tour', 'directory', 'information']}),
        ('Initial position', {'fields': ['initial_pan', 'initial_tilt']}),
        ('Vertical field of view limitation', {'fields': ['min_tilt', 'max_tilt']}),
    ]
    form = PanoramaAdminForm

class TourAdmin(admin.ModelAdmin):
    inlines = [PanoramaInline]

class ChainingAdminForm(forms.ModelForm):
    class Meta:
        model = Chaining

    def clean(self):
        cleaned_data = super(ChainingAdminForm, self).clean()
        from_panorama = cleaned_data.get('from_panorama')
        to_panorama = cleaned_data.get('to_panorama')
        if from_panorama.id == to_panorama.id:
            raise forms.ValidationError("Source and destination panoramas must be distinct")
        return cleaned_data

class ChainingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Panorama chaining', {'fields': ['from_panorama', 'to_panorama']}),
        ('Position', {'fields': ['pan', 'tilt']}),
        ('Options', {'fields': ['show_information']}),
    ]
    form = ChainingAdminForm

class HotspotInformationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['panorama', 'information']}),
        ('Position', {'fields': ['pan', 'tilt']}),
    ]

admin.site.register(Tour, TourAdmin)
admin.site.register(Panorama, PanoramaAdmin)
admin.site.register(Chaining, ChainingAdmin)
admin.site.register(InitialPanorama)
admin.site.register(HotspotInformation, HotspotInformationAdmin)

