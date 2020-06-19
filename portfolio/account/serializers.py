from .models import Account, Guest
from rest_framework import serializers

from django.core.paginator import Paginator
from django.http import JsonResponse


class AccountGetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(max_length = 100)
    email = serializers.EmailField()
    ip = serializers.CharField(max_length = 12)
    city = serializers.CharField(max_length = 255)
    country = serializers.CharField(max_length = 255)

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'ip', 'city', 'country']


class AccountSerializer(AccountGetSerializer):
    password = serializers.CharField(max_length = 100)

    def create(self, validated_data):
        return Account.register(validated_data)

    def update(self, instance, validated_data):
        return instance.update(instance, **validated_data)

    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'email', 'ip', 'city', 'country']


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only = True)
    ip = serializers.CharField(max_length = 12)
    city = serializers.CharField(max_length = 255)
    country = serializers.CharField(max_length = 255) 

    class Meta:
        model = Guest
        fields = ['id', 'ip', 'city', 'country']