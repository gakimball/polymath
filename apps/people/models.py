from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50, blank=True, help_text='Optional: write it like this: City, ST.')
    biography = models.TextField(blank=True, help_text='Optional.')

    photo = models.ImageField(blank=True, upload_to='images/people/photos', help_text='Optional.')
    background = models.ImageField(blank=True, upload_to='images/people/backgrounds', help_text='Optional.')

    email = models.EmailField('email address', blank=True, help_text='Optional.')
    twitter = models.TextField('twitter name', max_length=20, blank=True, help_text='Optional.')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'

        ordering = ['name']

class Credit(models.Model):
    ROLES = (
        ('generic', 'Generic'),
        ('Production', (
                ('production', 'Production'), 
                ('mixing', 'Mixing'), 
                ('writing', 'Writing'), 
                ('recording', 'Recording'),
            )
        ),
        ('Video', (
                ('camera', 'Camera'),
                ('editing', 'Editing'),
                ('postproduction', 'Post-production'),
            )
        ),
        ('Writing', (
                ('author', 'Author'),
                ('coauthor', 'Co-author'),
                ('editor', 'Editor'),
            )
        ),
        ('Strings', (
                ('guitar', 'Guitar'), 
                ('violin', 'violin'), 
                ('viloa', 'Viloa'), 
                ('cello', 'Cello'), 
                ('bass', 'Bass'), 
                ('bass_guitar', 'Bass Guitar'),
            )
        ),
        ('Percussion', (
                ('drums', 'Drums'), 
                ('vibraphone', 'Vibraphone'), 
                ('marimba', 'Marimba'),
            )
        ),
        ('Wind', (
                ('flute', 'Flute'),
            )
        ),
        ('Brass', (
                ('trumpet', 'Trumpet'), 
                ('trombone', 'Trombone'), 
                ('saxophone', 'Saxophone'),
            )
        ),
    )
    
    # ROLES = (
    #     ('mixing', 'Mixing'),
    #     ('recording', 'Recording'),
    # )

    person = models.ForeignKey('Person', help_text='Who did it?', related_name='credits')
    role = models.CharField(choices=ROLES, max_length=50, help_text='What\'d they do?')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        # return str(self.person) + ': ' + str(self.role) + ' for ' + str(self.content_object)
        return str(self.person) + ' on ' + str(self.content_object)