from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^polymath/', include('polymath.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # General
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^about/$', 'apps.people.views.about'),

    # Events
    url(r'calendar/$', TemplateView.as_view(template_name="events/calendar.html")),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Music
    url(r'^music/', 'apps.music.views.index'),
    url(r'^artists/(?P<artist_slug>[\w-]+)/$', 'apps.music.views.artist_detail'),
    url(r'^releases/(?P<album_id>[\d]+)/$', 'apps.music.views.release_detail'),
    url(r'^tracks/(?P<track_id>[\d]+)/$', 'apps.music.views.track_detail'),
    ## Music API
    url(r'^api/tracks/(?P<tracks>[0-9]+(,[0-9]+)*)', 'apps.music.views.get_playlist'),

    # Video
    url(r'^video/$', 'apps.video.views.index'),
    url(r'^video/(?P<video_id>[\d]+)/$', 'apps.video.views.video_detail'),
    url(r'^theouterspaces/$', 'apps.video.views.outerspaces'),

    # Writing
    url(r'^writing/$', 'apps.writing.views.index'),
    url(r'^read/(?P<story_id>[\d]+)/$', 'apps.writing.views.story_detail'),
    url(r'^zine/$', 'apps.writing.views.zine_index'),

    # Special
    url(r'^special/lethe/$', TemplateView.as_view(template_name="special/lethe.html")),
)

urlpatterns += staticfiles_urlpatterns()