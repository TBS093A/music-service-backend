from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404

from .models import TrackRating, AlbumRating, CommentRating
from .serializers import TrackRatingSerializer, AlbumRatingSerializer, CommentRatingSerializer

class TrackRatingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = TrackRating.objects.all()
    serializer_class = TrackRatingSerializer
    lookup_url_kwarg = 'user_id'

    def list(self, request, *args, **kwargs):
        trackID = self.kwargs.get('track_id')
        serializer = self.serializer_class.get_default(trackID)
        print(serializer)
        return Response(serializer)

    def create(self, request, *args, **kwargs):
        trackID = self.kwargs.get('track_id')
        checkValidate = self.serializer_class(data = request.data)
        if checkValidate and trackID is not None:
            serializer = self.serializer_class.create(request.data, track_id=trackID)
            return Response(serializer.toDict())
        return Response({ "ID": f"{trackID}" })

    def destroy(self, request, *args, **kwargs):
        trackID = self.kwargs.get('track_id')
        userID = self.kwargs.get(self.lookup_url_kwarg)
        return Response(self.serializer_class.delete(trackID, userID))

class AlbumRatingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = AlbumRating.objects.all()
    serializer_class = AlbumRatingSerializer
    lookup_url_kwarg = 'user_id'

    def get(self, request, *args, **kwargs):
        return Response("elo")

    def post(self, request, *args, **kwargs):
        return Response("elo")

    def delete(self, request, *args, **kwargs):
        return Response("elo")

class CommentRatingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = CommentRating.objects.all()
    serializer_class = CommentRatingSerializer
    lookup_url_kwarg = 'user_id'

    def get(self, request, *args, **kwargs):
        return Response("elo")

    def post(self, request, *args, **kwargs):
        return Response("elo")

    def delete(self, request, *args, **kwargs):
        return Response("elo")

