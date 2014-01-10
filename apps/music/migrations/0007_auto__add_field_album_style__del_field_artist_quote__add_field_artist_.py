# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Album.style'
        db.add_column(u'music_album', 'style',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Deleting field 'Artist.quote'
        db.delete_column(u'music_artist', 'quote')

        # Adding field 'Artist.deck'
        db.add_column(u'music_artist', 'deck',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Artist.soundcloud'
        db.add_column(u'music_artist', 'soundcloud',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Artist.bandcamp'
        db.add_column(u'music_artist', 'bandcamp',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Album.style'
        db.delete_column(u'music_album', 'style')

        # Adding field 'Artist.quote'
        db.add_column(u'music_artist', 'quote',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Artist.deck'
        db.delete_column(u'music_artist', 'deck')

        # Deleting field 'Artist.soundcloud'
        db.delete_column(u'music_artist', 'soundcloud')

        # Deleting field 'Artist.bandcamp'
        db.delete_column(u'music_artist', 'bandcamp')


    models = {
        u'music.album': {
            'Meta': {'ordering': "['-year', '-id']", 'object_name': 'Album'},
            'artists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'albums'", 'symmetrical': 'False', 'to': u"orm['music.Artist']"}),
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'compilation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'download_link': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flavor_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'release_type': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'reverse_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'music.artist': {
            'Meta': {'ordering': "['name']", 'object_name': 'Artist'},
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'bandcamp': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'deck': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'soundcloud': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'music.track': {
            'Meta': {'ordering': "['pub_date', 'id']", 'object_name': 'Track'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tracks'", 'null': 'True', 'to': u"orm['music.Album']"}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['music.Artist']"}),
            'audio_mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'audio_ogg': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'download_link': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'secondary_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'people.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.TextField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['music']