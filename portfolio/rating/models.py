from django.db import models
from django.utils.translation import ugettext_lazy
from rest_enumfield import EnumField
import enum

from portfolio.account.models import Account
from portfolio.comment.models import UserComment, GuestComment
from portfolio.album.models import Album, Track

from portfolio.utils import OneToManyModel

class RatingValue(enum.Enum):
    POSITIVE = 1
    NEGATIVE = -1

    __labels__ = {
        POSITIVE: ugettext_lazy('POSITIVE'),
        NEGATIVE: ugettext_lazy('NEGATIVE'),
    }


class AbstractRating(OneToManyModel):
    value = EnumField(choices=RatingValue)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


class CommentRating(AbstractRating):
    comment = models.ForeignKey(UserComment, on_delete=models.CASCADE)

    def toDict(self):
        return { 
            "id": self.id,
            "user_id": self.user_id,
            "value": self.value,
            "comment_id": self.comment_id
        }


class AlbumRating(AbstractRating):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def toDict(self):
        return { 
            "id": self.id,
            "user_id": self.user_id,
            "value": self.value,
            "album_id": self.album_id
        }

class TrackRating(AbstractRating):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def toDict(self):
        return { 
            "id": self.id,
            "user_id": self.user_id,
            "value": self.value,
            "track_id": self.track_id
        }