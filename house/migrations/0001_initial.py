# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Street'
        db.create_table('house_street', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='S', max_length=1, blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal('house', ['Street'])

        # Adding model 'House'
        db.create_table('house_house', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kult_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('ruwiki', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('name_alt', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('material', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('pasport', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('street', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['house.Street'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('coord_lon', self.gf('django.db.models.fields.FloatField')(max_length=20, null=True, blank=True)),
            ('coord_lat', self.gf('django.db.models.fields.FloatField')(max_length=20, null=True, blank=True)),
            ('pasport_address', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('safety', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('protection', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('pasport_safety', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('pasport_state', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('pasport_protection', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('usage', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('ownership', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('land_ownership', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('obligation', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('lease', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('tenant', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('chronology', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('documents', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('monitoring', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('complex', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('complex_root', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['house.House'], null=True, blank=True)),
            ('complex_name', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('complex_kult_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('extra_info', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('hidden_info', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('kult_checked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('kult_problems', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('gudea_checked', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('house', ['House'])

        # Adding model 'HousePhoto'
        db.create_table('house_housephoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['house.House'])),
            ('file', self.gf('yafotki.fields.YFField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal('house', ['HousePhoto'])

        # Adding model 'HousePassport'
        db.create_table('house_housepassport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['house.House'])),
            ('file', self.gf('yafotki.fields.YFField')(max_length=255)),
            ('page', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
        ))
        db.send_create_signal('house', ['HousePassport'])

        # Adding model 'HouseEvent'
        db.create_table('house_houseevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('house', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['house.House'])),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal('house', ['HouseEvent'])


    def backwards(self, orm):
        # Deleting model 'Street'
        db.delete_table('house_street')

        # Deleting model 'House'
        db.delete_table('house_house')

        # Deleting model 'HousePhoto'
        db.delete_table('house_housephoto')

        # Deleting model 'HousePassport'
        db.delete_table('house_housepassport')

        # Deleting model 'HouseEvent'
        db.delete_table('house_houseevent')


    models = {
        'house.house': {
            'Meta': {'object_name': 'House'},
            'chronology': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
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