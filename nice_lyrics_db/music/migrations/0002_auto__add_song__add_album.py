# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
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
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('music', ['Album'])

        # Adding M2M table for field artist on 'Album'
        db.create_table('music_album_artist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm['music.album'], null=False)),
            ('artist', models.ForeignKey(orm['music.artist'], null=False))
        ))
        db.create_unique('music_album_artist', ['album_id', 'artist_id'])


    def backwards(self, orm):
        
        # Deleting model 'Song'
        db.delete_table('music_song')

        # Removing M2M table for field artist on 'Song'
        db.delete_table('music_song_artist')

        # Deleting model 'Album'
        db.delete_table('music_album')

        # Removing M2M table for field artist on 'Album'
        db.delete_table('music_album_artist')


    models = {
        'music.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['music.Artist']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'music.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'music.song': {
            'Meta': {'object_name': 'Song'},
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['music.Artist']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['music']
