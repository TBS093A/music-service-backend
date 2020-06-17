from django.db import models
from account.models import Account


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.TextField()
    url_code = models.CharField(max_length=255)
    user = models.ManyToManyField(Account)
    