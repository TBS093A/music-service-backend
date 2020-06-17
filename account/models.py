from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import serializers


class AbstractUser(models.Model):
    city = models.CharField(verbose_name='City', max_length=255)
    country = models.CharField(verbose_name='Country', max_length=255)
    ip = models.CharField(verbose_name='IP', max_length=15)
    
    def fromDict(self, dict):
            self.__dict__.update(dict)

    class Meta:
        abstract = True


class Account(User, AbstractUser):
    
    def register(username, email, password):
        if Account.objects.get(username = username) is None and Account.objects.get(email = email) is None:
            Account.objects.create_user(username, email, password)
            return Response(f'Account created: ')

    def login(username, password) -> dict:
        tryLogin = authenticate(username = username, password = password)
        if tryLogin is not None:
            user = Account.objects.get(username = username)
            token = Token.objects.create(user = user)
            return token.__dict__
        else:
            return { error: 'login failed'}

    def logout():
        pass

    def update(self, userDict):
        self.fromDict(userDict)
        self.save


class Guest(AbstractUser):
    pass