# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Song'
        db.delete_table('music_song')

        # Removing M2M table for field artist on 'Song'
        db.delete_table('music_song_artist')

        # Deleting model 'Album'
        db.delete_table('music_album')

        # Removing M2M table for field artist on 'Album'
        db.delete_table('music_album_artist')

        # Adding model 'Disc'
        db.create_table('music_disc', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Release'])),
        ))
        db.send_create_signal('music', ['Disc'])

        # Adding model 'Release'
        db.create_table('music_release', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('tracks_count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('music', ['Release'])

        # Adding M2M table for field artist on 'Release'
        db.create_table('music_release_artist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['music.release'], null=False)),
            ('artist', models.ForeignKey(orm['music.artist'], null=False))
        ))
        db.create_unique('music_release_artist', ['release_id', 'artist_id'])

        # Adding model 'Track'
        db.create_table('music_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Release'])),
            ('disc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Disc'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('music', ['Track'])

        # Adding M2M table for field artist on 'Track'
        db.create_table('music_track_artist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('track', models.ForeignKey(orm['music.track'], null=False)),
            ('artist', models.ForeignKey(orm['music.artist'], null=False))
        ))
        db.create_unique('music_track_artist', ['track_id', 'artist_id'])


    def backwards(self, orm):
        
        # Adding model 'Song'
        db.create_table('music_song', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('music', ['Song'])

        # Adding M2M table for field artist on 'Song'
        db.create_table('music_song_artist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('song', models.ForeignKey(orm['music.song'], null=False)),
            ('artist', models.ForeignKey(orm['music.artist'], null=False))
        ))
        db.create_unique('music_song_artist', ['song_id', 'artist_id'])

        # Adding model 'Album'
        db.create_table('music_album', (
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('music', ['Album'])

        # Adding M2M table for field artist on 'Album'
        db.create_table('music_album_artist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm['music.album'], null=False)),
            ('artist', models.ForeignKey(orm['music.artist'], null=False))
        ))
        db.create_unique('music_album_artist', ['album_id', 'artist_id'])

        # Deleting model 'Disc'
        db.delete_table('music_disc')

        # Deleting model 'Release'
        db.delete_table('music_release')

        # Removing M2M table for field artist on 'Release'
        db.delete_table('music_release_artist')

        # Deleting model 'Track'
        db.delete_table('music_track')

        # Removing M2M table for field artist on 'Track'
        db.delete_table('music_track_artist')


    models = {
        'music.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'music.disc': {
            'Meta': {'object_name': 'Disc'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Release']"})
        },
        'music.release': {
            'Meta': {'object_name': 'Release'},
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['music.Artist']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tracks_count': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'music.track': {
            'Meta': {'object_name': 'Track'},
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['music.Artist']", 'symmetrical': 'False'}),
            'disc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Disc']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Release']"})
        }
    }

    complete_apps = ['music']
