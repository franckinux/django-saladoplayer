#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.templatetags.saladoplayer
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django import template

register = template.Library()

@register.inclusion_tag('saladoplayer/script.html', takes_context=True)
def saladoplayerscript(context, tour_id, hotspot, width, height):
    return {
        'tour_id': tour_id,
        'hotspot': hotspot,
        'width': width,
        'height': height,
        'saladoplayersettings': context['saladoplayersettings'],
    }

@register.inclusion_tag('saladoplayer/div.html', takes_context=True)
def saladoplayerdiv(context):
    return { 'saladoplayersettings': context['saladoplayersettings'] }

#references
#http://squeeville.com/2009/01/27/django-templatetag-requestcontext-and-inclusion_tag/
#https://github.com/ojii/django-classy-tags/issues/6