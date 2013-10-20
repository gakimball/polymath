from django.db import models
from django.template.defaultfilters import slugify
from durationfield.db.models.fields.duration import DurationField

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, help_text='Optional.')
    pub_date = models.DateField()

    series = models.ForeignKey('VideoSeries', blank=True, null=True)

    image = models.ImageField(blank=True, upload_to='videos/images', help_text='Optional, but seriously, upload one. 16:9 preferred.')
    length = models.CharField(max_length=5)
    
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
        if not self.image:
            self.image = 'placeholder/video.jpg'
        super(Video, self).save()

    class Meta:
        ordering = ['-pub_date']
        get_latest_by = ['pub_date']

class VideoSeries(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,help_text='Optional. Keep it to one paragraph.')
    image = models.ImageField(upload_to='videoseries/images',help_text='Promotional image for the series.')

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Video, self).save()

    class Meta:
        verbose_name = 'Video series'
        verbose_name_plural = 'Video series'