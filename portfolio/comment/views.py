from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework import permissions

from .models import UserComment, GuestComment
from .serializers import UserCommentSerializer, GuestCommentSerializer


class AnonAndUserPermissions(permissions.BasePermission):
    """
    Anonymous user always can create && User can modify self records only
    
    this is override of permissions in settings
    """
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return True
        return "AnonymousUser" != str(request.user)


class UserCommentViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer


class GuestCommentViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    
    queryset = GuestComment.objects.all()
    serializer_class = GuestCommentSerializer
    permission_classes = (AnonAndUserPermissions, )
