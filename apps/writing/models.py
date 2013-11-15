from django.db import models
from apps.people.models import Credit

# Create your models here.

class Story(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateField()

	GENRES = (
		('SS', 'Short Story'),
		('PO', 'Poetry'),
		('ES', 'Essay'),
		('SE', 'Series'),
	)
	category = models.CharField(choices=GENRES, max_length=2)
	series = models.ForeignKey('Collection', blank=True, null=True)
	image = models.ImageField(upload_to='stories/images/')

	body = models.TextField()

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-pub_date']
		get_latest_by = ['-pub_date']
		verbose_name_plural = 'Stories'

class Collection(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	year = models.IntegerField(max_length=4)
	image = models.ImageField(upload_to='collections/images/')
	background = models.ImageField(upload_to='collections/backgrounds/', blank=True, null=True)

	def __unicode__(self):
		return self.title