from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=256)


class Album(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    artist = models.ManyToManyField(Artist)

class Song(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ManyToManyField(Artist)
