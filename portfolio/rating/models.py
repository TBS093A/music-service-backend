from django.db import models
from django.utils.translation import ugettext_lazy
from django_enumfield import enum

from account.models import Account
from comment.models import UserComment, GuestComment
from album.models import Album
from song.models import Song


class RatingValue(enum.Enum):
    POSITIVE = 1
    NEGATIVE = 0

    __labels__ = {
        POSITIVE: ugettext_lazy('Positive'),
        NEGATIVE: ugettext_lazy('Negative'),
    }


class AbstractRating(models.Model):
    value = enum.EnumField(RatingValue)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


class CommentRating(AbstractRating):
    comment = models.ForeignKey(UserComment, on_delete=models.CASCADE)


class AlbumRating(AbstractRating):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class SongRating(AbstractRating):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
