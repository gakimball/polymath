from django.contrib import admin
from apps.music.models import Track, Album, Artist

def artists(obj):
  return ', '.join(str(item) for item in obj.artists.all())

def track_count(obj):
  return obj.tracks.count()

class TrackAdmin(admin.ModelAdmin):
  fieldsets = (
    ('Basics', {
      'fields': ('title', 'secondary_title', 'length', 'pub_date')
    }),
    ('Connections', {
      'fields': ('album', 'artist')
    }),
    ('Visual', {
      'fields': ('image', 'color')
    }),
    ('Files', {
      'fields': ('audio_mp3', 'audio_ogg', 'download_link')
    }),
  )
  list_display = ('title', 'artist', 'album', 'pub_date')
  ordering = ('-pub_date',)

class AlbumAdmin(admin.ModelAdmin):
  fieldsets = (
    ('Basics', {
      'fields': ('title', 'artists')
    }),
    ('Album info', {
      'fields': ('year', 'release_type', 'style', 'download_link')
    }),
    ('Visual', {
      'fields': ('image', 'reverse_image', 'color', 'flavor_text')
    }),
  )
  list_display = ('title', artists, 'year', track_count)

class ArtistAdmin(admin.ModelAdmin):
  fieldsets = (
    ('Basics', {
      'fields': ('name', 'owner')
    }),
    ('Info', {
      'fields': ('deck', 'biography')
    }),
    ('Visual', {
      'fields': ('image', 'background')
    }),
    ('External links', {
      'fields': ('email', 'facebook', 'twitter', 'soundcloud', 'bandcamp')
    }),
  )

admin.site.register(Track, TrackAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)