from django.db import models

from song.models import Song
from account.models import Account


class Playlist(models.Model):
    title = models.CharField(max_length=255)
    user = models.ManyToManyField(Account)
    song = models.ManyToManyField(Song)

