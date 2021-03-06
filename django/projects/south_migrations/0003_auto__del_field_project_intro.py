# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.intro'
        db.delete_column('projects_project', 'intro')


    def backwards(self, orm):
        # Adding field 'Project.intro'
        db.add_column('projects_project', 'intro',
                      self.gf('django.db.models.fields.TextField')(default='ADSDSDDs', unique=True, max_length=100),
                      keep_default=False)


    models = {
        'projects.pclass': {
            'Meta': {'object_name': 'PClass'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pclass_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pclass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.PClass']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'start': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_pic': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['projects']