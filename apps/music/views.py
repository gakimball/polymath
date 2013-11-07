from apps.music.models import Track, Album, Artist
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import Http404

def index(request):
    # Recent tracks
    track_count = 4
    track_list = Track.objects.only('title', 'artist', 'album', 'id').reverse()[:track_count]

    # Artists
    artist_list = Artist.objects.only('name', 'image')

    # Albums
    album_list = Album.objects.order_by('-year')

    # Data dictionary
    data_dict = {
        'track_list': track_list,
        'artist_list': artist_list,
        'album_list': album_list,
    }

    return render(request, 'music/index.html', data_dict)

def artist_detail(request, artist_slug):
    artist = get_object_or_404(Artist, slug=artist_slug)
    artist_list = Artist.objects.only('name')

    data_dict = {
        'artist': artist,
        'artist_list': artist_list,
    }

    return render(request, 'music/artist_detail.html', data_dict)

def release_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    more_albums = Album.objects.only('title', 'artists', 'image').order_by('?')[:4]

    data_dict = {
        'album': album,
        'more_albums': more_albums,
    }

    return render(request, 'music/releases/'+album.release_type+'.html', data_dict)

def track_detail(request, track_id):
    track = get_object_or_404(Track, pk=track_id)

    return render(request, 'music/track_detail.html', {'track': track, })