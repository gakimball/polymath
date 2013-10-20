from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=255)
	date = models.DateField()

	image = models.ImageField(blank=True, null=True, help_text='Optional: thumbnail/image for the event.')

	EVENT_TYPES = (
		('MU', 'Music'),
		('VI', 'Video'),
		('WR', 'Writing'),
		('AU', 'Audio'),
		('SH', 'Show'),
		('RE', 'Reading'),
		('SP', 'Special'),
	)

	event_type = models.CharField(max_length=2, choices=EVENT_TYPES, default='MU')

	location = models.CharField(max_length=30, blank=True)
	location_address = models.CharField(max_length=255, blank=True, help_text='Optional: this will build a Google Maps link on the site for you.')
	description = models.TextField(blank=True, help_text='Optional: only really necessary for special events.')

	link = models.URLField(blank=True, help_text='Optional: URL for more information, i.e. Facebook event page')
	link_action = models.CharField(max_length=30, help_text='Optional: text for link to above URL, default is "Learn more".')

	class Meta:
		ordering = ['date']

	def __unicode__(self):
		return self.name