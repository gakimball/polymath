from django.db import models
from django.contrib.contenttypes.models import ContentType
from apps.people.models import Person, Credit

# Create your models here.

class Story(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey('people.Person')
	# assoc_credit = models.ForeignKey('people.Credit', editable=False)
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

	# def save(self):
	# 	if not self.assoc_credit:
	# 		credit = Credit(person=self.author, role='author', content_object=self)
	# 		super(Story, self).save()
	# 		credit.save()
	# 		assoc_credit = credit
	# 	else:
	# 		credit = self.assoc_credit
	# 		credit.person = self.author
	# 		credit.save()

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