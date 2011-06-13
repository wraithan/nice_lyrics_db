from django.db import models


class Artist(models.Model):
    # Attributes
    name = models.CharField(max_length=256)


class Release(models.Model):
    # Attributes
    name = models.CharField(max_length=256)
    year = models.IntegerField()


class Track(models.Model):
    # Attributes
    name = models.CharField(max_length=256)
    number = models.IntegerField()
    lyrics = models.TextField()
    # Foriegn Keys
    artist = models.ManyToManyField(Artist)
    release = models.ForeignKey(Release)
