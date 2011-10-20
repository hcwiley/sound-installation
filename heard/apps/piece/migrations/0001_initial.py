# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MyImage'
        db.create_table('piece_myimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('piece', ['MyImage'])

        # Adding model 'Sound'
        db.create_table('piece_sound', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('piece', ['Sound'])

        # Adding model 'Location'
        db.create_table('piece_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('long', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('piece', ['Location'])

        # Adding model 'Piece'
        db.create_table('piece_piece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('default_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='piece_piece_default_image', null=True, to=orm['piece.MyImage'])),
            ('sounds', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='piece_piece_sound', null=True, to=orm['piece.Sound'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=160, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Artist'], null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['piece.Location'], null=True, blank=True)),
            ('show_map', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('use_street_view', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('heading', self.gf('django.db.models.fields.FloatField')(default=180.0)),
            ('pitch', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('zoom', self.gf('django.db.models.fields.FloatField')(default=1)),
            ('activation_code', self.gf('django.db.models.fields.CharField')(default='000', max_length=3)),
        ))
        db.send_create_signal('piece', ['Piece'])


    def backwards(self, orm):
        
        # Deleting model 'MyImage'
        db.delete_table('piece_myimage')

        # Deleting model 'Sound'
        db.delete_table('piece_sound')

        # Deleting model 'Location'
        db.delete_table('piece_location')

        # Deleting model 'Piece'
        db.delete_table('piece_piece')


    models = {
        'artist.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '400'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
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
        'piece.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'piece.myimage': {
            'Meta': {'ordering': "['image']", 'object_name': 'MyImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'piece.piece': {
            'Meta': {'object_name': 'Piece'},
            'activation_code': ('django.db.models.fields.CharField', [], {'default': "'000'", 'max_length': '3'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.Artist']", 'null': 'True', 'blank': 'True'}),
            'default_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'piece_piece_default_image'", 'null': 'True', 'to': "orm['piece.MyImage']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'heading': ('django.db.models.fields.FloatField', [], {'default': '180.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['piece.Location']", 'null': 'True', 'blank': 'True'}),
            'pitch': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'show_map': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '160', 'blank': 'True'}),
            'sounds': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'piece_piece_sound'", 'null': 'True', 'to': "orm['piece.Sound']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'use_street_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'zoom': ('django.db.models.fields.FloatField', [], {'default': '1'})
        },
        'piece.sound': {
            'Meta': {'object_name': 'Sound'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['piece']
