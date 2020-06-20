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

class SongRow(models.Model):
    rowNumber = models.IntegerField()
    gruop = models.BooleanField()
    leader = models.BooleanField()
    link = models.IntegerField(default=None)
    text = models.TextField()
    description = models.TextField()
    image = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def toDict(self):
        if self.link is not None:
            return {
                self.rowNumber: {
                    'group': self.gruop,
                    'leader': self.leader,
                    'link': self.link,
                    'text': self.text,
                }
            }
        else:
            return {
                self.rowNumber: {
                    'group': self.gruop,
                    'leader': self.leader,
                    'text': self.text,
                    'description': self.description,
                    'image': self.image
                }
            }