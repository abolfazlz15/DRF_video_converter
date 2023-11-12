from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from video.api import serializers
from video.models import VideoModel
from video.permissions import IsAuthor
from video.tasks import convert_video_task


class VideoUploadConvertView(APIView):
    def post(self, request, *args, **kwargs):
        file_uploaded = request.FILES.get('video_file')
        video_instance = VideoModel.objects.create(default_file=file_uploaded, user=request.user)

        video_id = convert_video_task.delay(video_instance.id).get()

        video_instance = VideoModel.objects.get(id=video_id)

        converted_file_url = request.build_absolute_uri(video_instance.convert_video.url)

        return Response({'converted_file_url': converted_file_url}, status=status.HTTP_201_CREATED)


class UserVideoListView(generics.ListAPIView):
    permission_classes = (IsAuthor,)
    serializer_class = serializers.UserVideoListSerializer

    def get_queryset(self):
        vidoo_instance =  VideoModel.objects.filter(user__id=self.kwargs['id'])
        self.check_object_permissions(self.request, vidoo_instance.first())
        return vidoo_instance