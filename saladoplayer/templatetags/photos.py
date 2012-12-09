#from https://gist.github.com/972090

from django import template
from django.db import models
from photologue.models import Photo

register = template.Library()
Photo = models.get_model('photologue', 'photo')

def photo_url(format_string):
    """Tries to load the appropriate Photologue Photo object by slug, and outputs
       the url to the display image.  If photo is not found, then returns an empty
       string."""
    try:
        photo = Photo.objects.get(title_slug=format_string, is_public=True)
        return photo.get_display_url()
    except Photo.DoesNotExist:
        return ''

register.simple_tag(photo_url)
