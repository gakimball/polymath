# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'video_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateField')()),
            ('series', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['video.VideoSeries'], null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('length', self.gf('durationfield.db.models.fields.duration.DurationField')()),
            ('service', self.gf('django.db.models.fields.CharField')(default='youtube', max_length=10)),
            ('videoid', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'video', ['Video'])

        # Adding model 'VideoSeries'
        db.create_table(u'video_videoseries', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'video', ['VideoSeries'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'video_video')

        # Deleting model 'VideoSeries'
        db.delete_table(u'video_videoseries')


    models = {
        u'video.video': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Video'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'length': ('durationfield.db.models.fields.duration.DurationField', [], {}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['video.VideoSeries']", 'null': 'True', 'blank': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'default': "'youtube'", 'max_length': '10'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'videoid': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        },
        u'video.videoseries': {
            'Meta': {'object_name': 'VideoSeries'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['video']