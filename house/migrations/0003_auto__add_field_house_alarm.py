# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'House.alarm'
        db.add_column('house_house', 'alarm',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'House.alarm'
        db.delete_column('house_house', 'alarm')


    models = {
        'house.cluster': {
            'Meta': {'ordering': "['name']", 'object_name': 'Cluster'},
            'geometry': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'house.house': {
            'Meta': {'object_name': 'House'},
            'alarm': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'chronology': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'cluster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['house.Cluster']", 'null': 'True', 'blank': 'True'}),
            'complex': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'complex_kult_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'complex_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'complex_root': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['house.House']", 'null': 'True', 'blank': 'True'}),
            'coord_lat': ('django.db.models.fields.FloatField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'coord_lon': ('django.db.models.fields.FloatField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'documents': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'extra_info': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'gudea_checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hidden_info': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kult_checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kult_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'kult_problems': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'land_ownership': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'lease': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'monitoring': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'name_alt': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'obligation': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'ownership': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'pasport': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pasport_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'pasport_protection': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'pasport_safety': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'pasport_state': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'protection': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ruwiki': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'safety': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'street': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['house.Street']"}),
            'tenant': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'usage': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'house.houseevent': {
            'Meta': {'object_name': 'HouseEvent'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['house.House']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'house.housepassport': {
            'Meta': {'object_name': 'HousePassport'},
            'file': ('yafotki.fields.YFField', [], {'max_length': '255'}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['house.House']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        },
        'house.housephoto': {
            'Meta': {'object_name': 'HousePhoto'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'file': ('yafotki.fields.YFField', [], {'max_length': '255'}),
            'house': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['house.House']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'house.street': {
            'Meta': {'ordering': "['name']", 'object_name': 'Street'},
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1', 'blank': 'True'})
        }
    }

    complete_apps = ['house']