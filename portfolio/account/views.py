from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Account, Guest
from .serializers import AccountSerializer, GuestSerializer, AccountGetSerializer


class AccountViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @swagger_auto_schema(responses={ 200: AccountGetSerializer })
    def retrieve(self, request, pk=None):
        print(pk)
        account = get_object_or_404(self.queryset, pk=pk)
        serializer = AccountGetSerializer(account)
        return Response(serializer.data)

    @swagger_auto_schema(responses={ 200: AccountGetSerializer })
    def list(self, request, *args, **kwargs):
        serializer = AccountGetSerializer(self.queryset, many=True)
        return Response(serializer.data)


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer




# @swagger_auto_schema(request_body = AccountSerializer, responses = {
    #     200: openapi.Response("OK", schema = AccountSerializer),
    #     400: openapi.Response("Empty")
    # })
