from django.contrib import admin
from apps.music.models import Track, Album, Artist

admin.site.register(Track)
admin.site.register(Album)
admin.site.register(Artist)