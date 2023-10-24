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
    class Meta:
        model = models.AlbumReview
        fields = ['user', 'album', 'content', 'score']

class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AlbumReviewLike
        fields = ['user', 'albumreview']