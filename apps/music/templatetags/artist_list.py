from django import template
from apps.music.models import Artist

register = template.Library()

@register.inclusion_tag('music/artist_list.html', takes_context=True)
def artist_list(context):
    # Artist list
    artist_list = Artist.objects.only('id', 'name', 'image', 'slug')

    return {
        'artist_list': artist_list
    }