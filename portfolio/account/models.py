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
    
    @staticmethod
    def register(userDict) -> object:
        account = Account.objects.create_user(
            userDict['username'], 
            userDict['email'], 
            userDict['password'],
        )
        account.ip = userDict['ip']
        account.city = userDict['city'],
        account.country = userDict['country']
        account.save()
        return account

    def login(self, username, password) -> dict:
        tryLogin = authenticate(username = username, password = password)
        if tryLogin is not None:
            user = Account.objects.get(username = username)
            token = Token.objects.create(user = user)
            return token.__dict__
        else:
            return { 'error': 'login failed'}

    def logout(self):
        pass

    def update(self, userDict):
        if 'password' in userDict:
            password = userDict.pop('password')
            self.set_password(password)
        self.fromDict(userDict)
        self.save()            

    def set_password(self, raw_password):
        return super().set_password(raw_password)


class Guest(AbstractUser):
    pass
    
