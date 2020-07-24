from rest_framework import serializers

from .models import UserComment, GuestComment

class UserCommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    text = serializers.CharField()

    class Meta:
        model = UserComment
        fields = [ 'id', 'user_id', 'text']

class GuestCommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    guest_id = serializers.IntegerField()
    text = serializers.CharField()

    class Meta:
        model = GuestComment
        fields = [ 'id', 'guest_id', 'text']