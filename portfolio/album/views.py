from django.shortcuts import render

from rest_framework import viewsets

from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackRowViewSet(viewsets.ModelViewSet):
    queryset = TrackRow.objects.all()
    serializer_class = TrackRowSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
