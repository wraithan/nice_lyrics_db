from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=256)


class Release(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    artist = models.ManyToManyField(Artist)
    language = models.CharField(max_length=256)
    tracks_count = models.IntegerField()


class Disc(models.Model):
    release = models.ForeignKey(Release)


class Track(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ManyToManyField(Artist)
    release = models.ForeignKey(Release)
    disc = models.ForeignKey(Disc)
    number = models.IntegerField()
