from django import template
from apps.music.models import Album, Track

register = template.Library()

@register.inclusion_tag('music/related_music.html', takes_context=True)
def related_music(context):
    # Albums from this artist, except the one the page is referencing
    album_list = Album.objects.only('title', 'image').filter(pk=context['track'].album.id)

    # Random tracks from other artists
    track_list = Track.objects.exclude(artist__pk=context['track'].artist.id).order_by('?')[:4]

    # Random samples of other media
    # TODO

    return {
        'track': context['track'],
        'album_list': album_list,
        'track_list': track_list,
    }