from django import template
from apps.music.models import Album

register = template.Library()

@register.inclusion_tag('music/templatetags/album.html')
def album(album_id):
    # Artist list
    try:
      album = Album.objects.only('title', 'year', 'image', 'download_link').get(pk=album_id)
      return {
          'album': album
      }
    except:
      pass