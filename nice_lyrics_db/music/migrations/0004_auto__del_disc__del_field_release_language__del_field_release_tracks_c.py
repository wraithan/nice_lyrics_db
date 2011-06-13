# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Disc'
        db.delete_table('music_disc')

        # Deleting field 'Release.language'
        db.delete_column('music_release', 'language')

        # Deleting field 'Release.tracks_count'
        db.delete_column('music_release', 'tracks_count')

        # Removing M2M table for field artist on 'Release'
        db.delete_table('music_release_artist')

        # Deleting field 'Track.disc'
        db.delete_column('music_track', 'disc_id')

        # Adding field 'Track.lyrics'
        db.add_column('music_track', 'lyrics', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Disc'
        db.create_table('music_disc', (
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Release'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('music', ['Disc'])

        # Adding field 'Release.language'
        db.add_column('music_release', 'language', self.gf('django.db.models.fields.CharField')(default='', max_length=256), keep_default=False)

        # Adding field 'Release.tracks_count'
        db.add_column('music_release', 'tracks_count', self.gf('django.db.models.fields.IntegerField')(default=''), keep_default=False)

        # Adding M2M table for field artist on 'Release'
        db.create_table('music_release_artist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['music.release'], null=False)),
            ('artist', models.ForeignKey(orm['music.artist'], null=False))
        ))
        db.create_unique('music_release_artist', ['release_id', 'artist_id'])

        # User chose to not deal with backwards NULL issues for 'Track.disc'
        raise RuntimeError("Cannot reverse this migration. 'Track.disc' and its values cannot be restored.")

        # Deleting field 'Track.lyrics'
        db.delete_column('music_track', 'lyrics')


    models = {
        'music.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'music.release': {
            'Meta': {'object_name': 'Release'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'music.track': {
            'Meta': {'object_name': 'Track'},
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['music.Artist']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lyrics': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Release']"})
        }
    }

    complete_apps = ['music']
