from django.db import models

from album.models import Track
from account.models import Account


class Playlist(models.Model):
    title = models.CharField(max_length=255)
    user = models.ManyToManyField(Account)
    track = models.ManyToManyField(Track)

