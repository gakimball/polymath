from django.contrib import admin
from apps.music.models import Track, Album, Artist

def artists(obj):
  return ', '.join(str(item) for item in obj.artists.all())

def track_count(obj):
  return obj.tracks.count()

class TrackAdmin(admin.ModelAdmin):
  list_display = ('title', 'artist', 'album', 'pub_date')
  ordering = ('-pub_date',)

class AlbumAdmin(admin.ModelAdmin):
  list_display = ('title', artists, 'year', track_count)

admin.site.register(Track, TrackAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist)