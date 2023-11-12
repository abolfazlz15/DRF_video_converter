from rest_framework import serializers

from video.models import VideoModel


class UserVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModel
        fields = ('id', 'default_file', 'convert_video')