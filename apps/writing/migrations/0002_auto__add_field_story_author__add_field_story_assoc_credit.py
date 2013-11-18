# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Story.author'
        db.add_column(u'writing_story', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['people.Person']),
                      keep_default=False)

        # Adding field 'Story.assoc_credit'
        db.add_column(u'writing_story', 'assoc_credit',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['people.Credit']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Story.author'
        db.delete_column(u'writing_story', 'author_id')

        # Deleting field 'Story.assoc_credit'
        db.delete_column(u'writing_story', 'assoc_credit_id')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'people.credit': {
            'Meta': {'object_name': 'Credit'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'credits'", 'to': u"orm['people.Person']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        },
        u'writing.collection': {
            'Meta': {'object_name': 'Collection'},
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        u'writing.story': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Story'},
            'assoc_credit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Credit']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['writing.Collection']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['writing']