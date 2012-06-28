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
        ('', {'fields': ['panorama', 'information']}),
        ('Position', {'fields': ['pan', 'tilt']}),
    ]

admin.site.register(Tour, TourAdmin)
admin.site.register(Panorama)
admin.site.register(Chaining, ChainingAdmin)
admin.site.register(InitialPanorama)
admin.site.register(HotspotInformation, HotspotInformationAdmin)

