from django.db import models

from django.db import models
from django.template.defaultfilters import slugify

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, help_text='Optional.')
    pub_date = models.DateField()

    series = models.ForeignKey('VideoSeries', blank=True, null=True)

    image = models.ImageField(blank=True, upload_to='videos/images', help_text='Optional, but seriously, upload one. 16:9 preferred.')
    background = models.ImageField(blank=True, upload_to='videos/backgrounds', help_text='Background image for video\'s page')
    length = models.CharField(max_length=5, help_text='Write it like this: "3:04". No leading zeroes in the minutes place.')
    
    VIDEO_SERVICES = (
        ('youtube', 'YouTube'),
        ('vimeo', 'Vimeo'),
    )

    service = models.CharField(max_length=10, choices=VIDEO_SERVICES, default='youtube')
    videoid = models.CharField(max_length=11, help_text='The ID of the video. (it\'s a string of letters and numbers at the end of the URL.')

    slug = models.SlugField(editable=False)

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        if not self.thumbnail:
            self.thumbnail = 'placeholder/video.jpg'
        super(Video, self).save()

    class Meta:
        ordering = ['-pub_date']
        get_latest_by = ['pub_date']

class VideoSeries(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,help_text='Optional. Keep it to one paragraph.')
    image = models.ImageField(upload_to='videos/series/images',help_text='Promotional image for the series.')

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Video, self).save()

    class Meta:
        verbose_name = 'Video series'
        verbose_name_plural = 'Video series'