from rest_framework import serializers
from rest_enumfield import EnumField

from .models import *

class TrackRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user_id = serializers.IntegerField()

    @staticmethod
    def get_default(track_id):
        queryset = TrackRating.objects.filter(track_id=track_id)
        return [ x.toDict() for x in queryset ]

    @staticmethod
    def create(validated_data, track_id):
        validated_data["track_id"] = track_id    
        return TrackRating.create(TrackRating, validated_data)

    @staticmethod
    def delete(track_id, user_id):
        return TrackRating.objects.get(track_id=track_id, user_id=user_id).delete()

    class Meta:
        model = TrackRating
        fields = ['id', 'user_id', 'value']


class UserCommentRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user_id = serializers.IntegerField()

    @staticmethod
    def get_default(comment_id):
        queryset = UserCommentRating.objects.filter(comment_id=comment_id)
        return [ x.toDict() for x in queryset ]

    @staticmethod
    def create(validated_data, comment_id):
        validated_data["comment_id"] = comment_id    
        return UserCommentRating.create(UserCommentRating, validated_data)

    @staticmethod
    def delete(comment_id, user_id):
        return UserCommentRating.objects.get(comment_id=comment_id, user_id=user_id).delete()

    class Meta:
        model = UserCommentRating
        fields = ['id', 'user_id', 'value']


class AlbumRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user_id = serializers.IntegerField()

    @staticmethod
    def get_default(album_id):
        queryset = AlbumRating.objects.filter(album_id=album_id)
        return [ x.toDict() for x in queryset ]

    @staticmethod
    def create(validated_data, album_id):
        validated_data["album_id"] = album_id    
        return AlbumRating.create(AlbumRating, validated_data)

    @staticmethod
    def delete(album_id, user_id):
        return AlbumRating.objects.get(album_id=album_id, user_id=user_id).delete()


    class Meta:
        model = AlbumRating
        fields = ['id', 'user_id', 'value']
        
        