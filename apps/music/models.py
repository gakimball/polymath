from django.db import models
from apps.people.models import Person

from operator import attrgetter
from itertools import chain
from django.db import models
from django.template.defaultfilters import slugify

class Track(models.Model):
    # Basics
    title = models.CharField(max_length=255, help_text='Title of the track.')
    secondary_title = models.CharField(max_length=255, blank=True, help_text='Optional: an alternate title for a track or a "featuring" line.')
    length = models.CharField(max_length=5,help_text='Write it like this: "3:04". No leading zeroes in the minutes place.')
    pub_date = models.DateField('publish date', help_text='Release date for this track. It\'s probably today, right?')

    # Connections
    album = models.ForeignKey('Album', null=True, blank=True, help_text='The album this track is part of. Leave this blank if the track is a single.', related_name='tracks')
    artist = models.ForeignKey('Artist', help_text='The artist for this track. It\'s probably the same as the album\'s artist, unless we\'re talking about a collaboration album.')

    # Visual
    image = models.ImageField(blank=True,upload_to='tracks/images/',help_text='Optional: unique cover art for this track. If your track is a single, you need to put an image here.')
    color = models.CharField(max_length=6, blank=True, help_text='Optional: accent color for track.')
    
    # Files
    audio_mp3 = models.FileField(upload_to='tracks/mp3/',null=True,blank=True,help_text='Track in .mp3 format.')
    audio_ogg = models.FileField(upload_to='tracks/ogg/',null=True,blank=True,help_text='Track in .oga format.')
    download_link = models.FileField(upload_to='tracks/zip/',null=True,blank=True,help_text='Track in a .zip file.')

    # Backend
    file_size = models.IntegerField(editable=False,null=True,blank=True)
    hidden = models.BooleanField(editable=False)
    slug = models.SlugField(editable=False)

    # Unused
    background = models.ImageField(blank=True, editable=False, upload_to='tracks/backgrounds/',help_text='Optional, but please upload one: background image for use on the track\'s page and on the home page carousel.')
    description = models.TextField(blank=True, editable=False, help_text='Optional: write something about this track.')

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        if self.download_link:
            try:
                self.file_size = self.download_link.size / 1024
            except OSError:
                pass
        super(Track, self).save()

    class Meta:
        ordering = ['pub_date', 'id']
        get_latest_by = ['pub_date']

    # Checks to see if a track is a single
    def is_single(self):
        return not self.album

    # Returns the track's cover if it has one, otherwise the album's cover
    def cover(self):
        if self.image:
            return self.image.url
        elif self.album.image:
            return self.album.image.url

class Album(models.Model):
    RELEASE_TYPES = (
        ('album', 'Album'),
        ('single', 'Single'),
        ('split', 'Split'),
    )

    # Basics
    title = models.CharField(max_length=255, help_text='Title of the album.')
    artists = models.ManyToManyField('Artist', help_text='Artist for the album. If it\'s a compilation you can add more than one.', related_name='albums')

    # Album info
    year = models.CharField('release year', max_length=4, help_text='Four digits, please.')
    release_type = models.CharField(max_length=6, choices=RELEASE_TYPES, help_text='Release type determines the format of the page.')
    style = models.CharField(max_length=20, blank=True)

    # Visual
    image = models.ImageField(upload_to='albums/images/', help_text='Album art goes here. However, when you add a track, each track may have its own picture as well.')
    reverse_image = models.ImageField(upload_to='albums/reverse_images/', blank=True, null=True, help_text='Optional: back side of cover art.')
    color = models.CharField(max_length=6, blank=True, help_text='Optional: accent color for album.')
    flavor_text = models.CharField(max_length=50, blank=True, help_text='Optional: flavor text to display above album title.')

    # Files
    download_link = models.FileField(upload_to='albums/zip/', blank=True, null=True, help_text='Optional: .zip file of album. Don\'t upload it until the entire album has been released for streaming.')

    # Backend
    file_size = models.IntegerField(editable=False, blank=True, null=True)

    # Unused
    background = models.ImageField(upload_to='albums/backgrounds/', blank=True, help_text='NOT IN UUUUSE.')
    compilation = models.BooleanField(default=False, editable=False)
    description = models.TextField(blank=True, help_text='Optional: keep it to one paragraph.')

    class Meta:
        ordering = ['-year', '-id']
        get_latest_by = ['year']

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.id:
            self.stats_downloads = 0
        if not self.image:
            self.image = 'placeholder/album.jpg'
        if self.download_link:
            try:
                self.file_size = self.download_link.size
            except OSError:
                pass
        super(Album, self).save()
        if self.artists.count() > 1:
            self.compilation = True
        else:
            self.compilation = False
        super(Album, self).save()

class Artist(models.Model):
    # Basics
    name = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey('people.Person', null=True, blank=True, help_text='Who\'s project is this?')

    # Info
    deck = models.TextField(blank=True, help_text='[This band] is...')
    biography = models.TextField(blank=True, help_text='Optional: one paragraph only for now.')

    # Visual
    image = models.ImageField(blank=True, upload_to='artists/images', help_text='Main artist photo.')
    background = models.ImageField(blank=True,upload_to='artists/backgrounds/',help_text='Optional, but come on: background image for artist.')

    # External links
    email = models.EmailField('email address', help_text="Optional: email address for artist", blank=True)
    twitter = models.CharField('twitter name', max_length=30, help_text="Optional: Twitter username without the @ sign", blank=True)
    facebook = models.URLField('facebook page', help_text="Optional: full URL of Facebook page", blank=True)
    soundcloud = models.URLField('soundcloud page', blank=True)
    bandcamp = models.URLField('bandcamp page', blank=True)

    # Backend
    slug = models.SlugField(editable=False)
    
    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        if not self.image:
            self.image = 'placeholder/artist.jpg'
        super(Artist, self).save()