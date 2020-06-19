from django.db import models

from account.models import Account
from album.models import Album

class Song(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    text = models.TextField()
    image = models.TextField()
    audio = models.TextField()
    url_code = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
