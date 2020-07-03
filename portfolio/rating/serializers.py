from rest_framework import serializers
from rest_enumfield import EnumField

from .models import *

class TrackRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user_id = serializers.IntegerField()
    value = EnumField(
        choices=RatingValue, 
        to_choice=lambda x:(x.name, x.value),
        to_repr=lambda x: x
    )
    # track_id = serializers.IntegerField()

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


class CommentRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user_id = serializers.IntegerField()
    value = EnumField(
        choices=RatingValue, 
        to_choice=lambda x:(x.name, x.value),
        to_repr=lambda x: x
    )
    # comment_id = serializers.IntegerField()

    def create(self, validated_data):
        return CommentRating.create(TrackRating, validated_data)

    def update(self, instance, validated_data):
        return instance.update(validated_data)

    class Meta:
        model = CommentRating
        fields = ['id', 'user_id', 'value']


class AlbumRatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user_id = serializers.IntegerField()
    value = EnumField(
        choices=RatingValue, 
        to_choice=lambda x:(x.name, x.value),
        to_repr=lambda x: x
    )
    # album_id = serializers.IntegerField()

    def create(self, validated_data):
        return AlbumRating.create(TrackRating, validated_data)

    def update(self, instance, validated_data):
        return instance.update(validated_data)

    class Meta:
        model = AlbumRating
        fields = ['id', 'user_id', 'value']
        
        