from datetime import timedelta
import tempfile
from io import BytesIO
from django.utils import timezone

from celery import shared_task
from django.core.files.base import ContentFile
from moviepy.editor import VideoFileClip

from video.models import VideoModel


@shared_task
def convert_video_task(video_id):
    video_instance = VideoModel.objects.get(id=video_id)

    video_clip = VideoFileClip(video_instance.default_file.path)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
        video_clip.audio.write_audiofile(temp_audio_file.name, codec='pcm_s16le')

        with open(temp_audio_file.name, 'rb') as temp_file:
            converted_file_content = BytesIO(temp_file.read())

    # Save the converted file to the VideoModel instance
    video_instance.convert_video.save(f'converted_audio_{video_instance.default_file.name}.wav', ContentFile(converted_file_content.getvalue()))
    video_instance.save()

    return video_instance.id


@shared_task
def delete_expire_video_task():
    one_day_ago = timezone.now() - timedelta(hours=12)
    old_objects = VideoModel.objects.filter(created_at__lt=one_day_ago)
    old_objects.delete()