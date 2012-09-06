# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timer'
        db.create_table('pos_timer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('structure', self.gf('django.db.models.fields.BigIntegerField')(default=21644)),
            ('timer', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('location_id', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('location', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('moon_id', self.gf('django.db.models.fields.BigIntegerField')(default=0, null=True, blank=True)),
            ('moon', self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cycle', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('friendly', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('owner_id', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
        ))
        db.send_create_signal('pos', ['Timer'])


    def backwards(self, orm):
        # Deleting model 'Timer'
        db.delete_table('pos_timer')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pos.fuellevel': {
            'Meta': {'ordering': "['pos', 'date', 'type_id']", 'object_name': 'FuelLevel'},
            'consumption': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pos': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fuel_levels'", 'to': "orm['pos.POS']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'type_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'pos.pos': {
            'Meta': {'object_name': 'POS'},
            'allow_alliance_members': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_corporation_members': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attack_on_aggression': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attack_on_concord_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'attack_on_corp_war': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'authorized_groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'visible_group'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'cached_until': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'custom_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'deploy_flags': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'fuel_type_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'has_sov': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item_id': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'location_id': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'moon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'moon_id': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'online_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'operators': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'operated_poses'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'security_status_threshold': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'standings_threshold': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'state_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'type_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'usage_flags': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'use_standings_from': ('django.db.models.fields.BigIntegerField', [], {'default': '0'})
        },
        'pos.timer': {
            'Meta': {'object_name': 'Timer'},
            'cycle': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'friendly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'location_id': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'moon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'moon_id': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner_id': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'structure': ('django.db.models.fields.BigIntegerField', [], {'default': '21644'}),
            'timer': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['pos']