from django.shortcuts import render

from rest_framework import viewsets

from .models import *
from .serializers import *


class TrackViewSet(viewsets.ModelViewSet):
    """
    A Tack CRUD (abstract from `viewsets.ModelViewSet`):
        `GET`: `list()`
        `GET`: `retrieve()` /parameter {id}
        `POST`: `create()`
        `PUT`&`PATCH`: `update()` /parameter {id}
        `DELETE`: `destroy()` /parameter {id}
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackRowViewSet(viewsets.ModelViewSet):
    """
    A TrackRow CRUD (abstract from `viewsets.ModelViewSet`):
        `GET`: `list()`
        `GET`: `retrieve()` /parameter {id}
        `POST`: `create()`
        `PUT`&`PATCH`: `update()` /parameter {id}
        `DELETE`: `destroy()` /parameter {id}
    """
    queryset = TrackRow.objects.all()
    serializer_class = TrackRowSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    A Album CRUD (abstract from `viewsets.ModelViewSet`):
        `GET`: `list()`
        `GET`: `retrieve()` /parameter {id}
        `POST`: `create()`
        `PUT`&`PATCH`: `update()` /parameter {id}
        `DELETE`: `destroy()` /parameter {id}
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
