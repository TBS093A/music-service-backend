from django.db import models

from portfolio.account.models import Account, Guest


class AbstractComment(models.Model):
    text = models.CharField(max_length=255)
    
    class Meta:
        abstract = True


class UserComment(AbstractComment):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)


class GuestComment(AbstractComment):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
