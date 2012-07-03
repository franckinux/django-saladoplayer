#!/usr/bin/env python
# -*- coding: utf8 -*-

"""saladoplayer.context_processors
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.conf import settings as proj_settings

def settings(request):
    return {
        'saladoplayersettings': {
            'url': proj_settings.SALADOPLAYER_STATIC_URL,
            'debug': proj_settings.SALADOPLAYER_DEBUG,
            'viewfinder': proj_settings.SALADOPLAYER_VIEWFINDER,
            'secure': proj_settings.SALADOPLAYER_FLASH_SECURE,
            'branding': proj_settings.SALADOPLAYER_SHOW_BRANDING,
        }
    }