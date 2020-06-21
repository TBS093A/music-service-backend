from rest_framework import serializers

from rest_framework.reverse import reverse

from .models import *


class TrackRowSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    track_id = serializers.IntegerField()
    row_number = serializers.IntegerField()
    group = serializers.BooleanField()
    leader = serializers.BooleanField()
    link = serializers.IntegerField()
    text = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()

    def create(self, validated_data):
        return TrackRow.create(TrackRow, validated_data)

    def update(self, instance, validated_data):
        return instance.update(validated_data)

    class Meta:
        model = TrackRow
        fields = ['id', 'track_id','row_number', 'group', 'leader', 'link', 'text', 'description', 'image']


class TrackSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    album_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000)
    text = serializers.CharField()
    image = serializers.CharField()
    audio = serializers.CharField()
    url_code = serializers.CharField(max_length=255)
    track_rows = TrackRowSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Track.create(Track, validated_data)

    def update(self, instance, validated_data):
        return instance.update(validated_data)
    
    # track_rows = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='row_number'
    # )

    # view_name = 'track'
    # queryset = Track.objects.all()

    # def get_url(self, obj, view_name, request, format):
    #     url_kargs = {
    #         'album_id': obj.album.id,
    #         'id': obj.id
    #     }
    #     return reverse(view_name, kwargs=url_kargs, request=request, format=format)

    # def get_object(self, view_name, view_args, view_kwargs):
    #     lookup_kwargs = {
    #         'album_id': view_kwargs['album_id'],
    #         'id': view_kwargs['id']
    #     }
    #     return self.get_queryset().get(**lookup_kwargs)


    class Meta:
        model = Track
        fields = ['id', 'album_id', 'user_id', 'title', 'description', 'text', 'image', 'audio', 'url_code', 'track_rows']


class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    image = serializers.CharField()
    url_code = serializers.CharField(max_length=255)
    tracks = TrackSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Album.create(Album, validated_data)

    def update(self, instance, validated_data):
        return Album.update(validated_data)

    class Meta:
        model = Album
        fields = ['id', 'user_id', 'title', 'description', 'image', 'url_code', 'tracks']



# Relations


# class TrackTrackRowRelation(serializers.RelatedField):
#     def to_representation(self, value):
#         serializer = TrackSerializer(value.get_queryset()[0])
#         return serializer.data


# class AlbumTrackRelation(serializers.RelatedField):
#     def to_representation(self, value):
#         serializer = AlbumSerializer(value.get_queryset()[0])
#         return serializer.data

    
# class TrackRowSerializerFull(TrackRowSerializer):
#     """
#     TrackRow + Track id
#     """
#     track_id = TrackTrackRowRelation(queryset=Track.objects.all())

#     class Meta:
#         model = TrackRow
#         fields = ['id', 'track_id', 'row_number', 'group', 'leader', 'link', 'text', 'description', 'image']


# class TrackSerializerFull(TrackSerializer):
#     """
#     Track + Album id
#     """
#     album_id = AlbumTrackRelation(queryset=Album.objects.all())

#     def create(self, validated_data):
#         return super().create(validated_data)

#     class Meta:
#         model = Track
#         fields = ['id', 'album_id', 'title', 'description', 'text', 'image', 'audio', 'url_code', 'track_rows']
