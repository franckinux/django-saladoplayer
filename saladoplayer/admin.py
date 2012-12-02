#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.admin
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.contrib import admin
from django import forms
from saladoplayer.models import Tour, Panorama, Chaining, HotspotInformation

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
                    raise forms.ValidationError("Initial tilt must be greater than min_tilt")
            if max_tilt:
                if  max_tilt < initial_tilt:
                    raise forms.ValidationError("Initial tilt must be lower than max_tilt")
        return cleaned_data

class PanoramaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields': ['tour', 'directory', 'information']}),
        ('Initial position', {'fields': ['initial_pan', 'initial_tilt']}),
        ('Vertical field of view limitation', {'fields': ['min_tilt', 'max_tilt']}),
    ]
    form = PanoramaAdminForm

class TourAdminForm(forms.ModelForm):
    class Meta:
        model = Tour

    def clean(self):
        cleaned_data = super(TourAdminForm, self).clean()
        facebook = cleaned_data.get("facebook")
        description = cleaned_data.get("description")
        thumb = cleaned_data.get("thumb")
        if facebook and not (description and thumb):
            raise forms.ValidationError("A description and a thumb image are needed to be included in Facebook metadata")
        return cleaned_data


class TourAdmin(admin.ModelAdmin):
    inlines = [PanoramaInline]
    fieldsets = [
        ('', {'fields': ['title', 'title_slug', 'first_panorama']}),
        ('Tour options', {'fields': ['display_dropmenu', 'auto_rotation', 'display_viewfinder']}),
        ('FaceBook metadata', {'fields': ['facebook', 'description', 'thumb']}),
    ]
    prepopulated_fields = {'title_slug': ('title',)}
    form = TourAdminForm

class ChainingAdminForm(forms.ModelForm):
    class Meta:
        model = Chaining

    def clean(self):
        cleaned_data = super(ChainingAdminForm, self).clean()
        from_panorama = cleaned_data.get('from_panorama')
        to_panorama = cleaned_data.get('to_panorama')
        if from_panorama.id == to_panorama.id:
            raise forms.ValidationError("Source and destination panoramas must be distinct")
        if from_panorama.tour.id != to_panorama.tour.id:
            raise forms.ValidationError("Source and destination panoramas must belong to the same tour")
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
admin.site.register(HotspotInformation, HotspotInformationAdmin)

