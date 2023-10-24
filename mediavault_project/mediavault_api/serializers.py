from rest_framework import serializers
from . import models

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Band
        fields = ['name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = ['name', 'band']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ['name', 'duration', 'album']


class AlbumReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='album.id')

    class Meta:
        model = models.AlbumReview
        fields = ['username', 'user_id', 'post', 'album', 'content', 'score']
