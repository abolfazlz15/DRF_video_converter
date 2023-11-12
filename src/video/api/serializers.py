from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers

from video.models import VideoModel


class UserVideoListSerializer(serializers.ModelSerializer):
    expire_time = serializers.SerializerMethodField()
    class Meta:
        model = VideoModel
        fields = ('id', 'default_file', 'convert_video', 'expire_time')
    
    def get_expire_time(self, obj):
        deletion_time = obj.created_at + timedelta(hours=12)

        current_time = timezone.now()
        time_left = deletion_time - current_time

        return str(time_left)