from django.db import models

from portfolio.account.models import Account
from portfolio.utils import OneToManyModel

class Album(OneToManyModel):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.TextField()
    url_code = models.CharField(max_length=255)
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING)


class Track(OneToManyModel):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    text = models.TextField()
    image = models.TextField()
    audio = models.TextField()
    url_code = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)


class TrackRow(OneToManyModel):
    row_number = models.IntegerField()
    group = models.BooleanField()
    leader = models.BooleanField()
    link = models.IntegerField(default=None)
    text = models.TextField(default=None)
    description = models.TextField(default=None)
    image = models.TextField(default=None)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def toDict(self):
        if self.link is not None:
            return {
                self.row_number: {
                    'group': self.gruop,
                    'leader': self.leader,
                    'link': self.link,
                    'text': self.text,
                    'description': None,
                    'image': None
                }
            }
        else:
            return {
                self.row_number: {
                    'group': self.gruop,
                    'leader': self.leader,
                    'link': None,
                    'text': None,
                    'description': self.description,
                    'image': self.image
                }
            }
    