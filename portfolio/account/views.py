from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.views import ObtainAuthToken

from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404

from .models import Account, Guest
from .serializers import *


class AnonAndUserPermissions(permissions.BasePermission):
    """
    Anonymous user always can create && User can modify self records only
    
    this is override of permissions in settings
    """
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        return str(obj.username) == str(request.user)


class AccountViewSet(viewsets.ModelViewSet):
    """
    A User CRUD `retrieve()`, `list()` and abstract `create()` (`create()` is register)
    and  `update()` from class `ModelViewSet` in viewsets
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (AnonAndUserPermissions, )

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


class AccountAuth(ObtainAuthToken):
    """
    A User Authorization `login()`, `logout()`
    """
    queryset = Account.objects.all()
    serializer_class = AccountAuthSerializer

    @swagger_auto_schema(
        responses={ 200: '{ Token: Authorize }' },
        request_body=AccountAuthSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        return Response(AccountAuthSerializer.login(username, password))
    
    @swagger_auto_schema(responses={ 200: '{ info: logout }' })
    def delete(self, request, *args, **kwargs):
        return Response(self.serializer_class.logout(request))


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = (AnonAndUserPermissions, )
