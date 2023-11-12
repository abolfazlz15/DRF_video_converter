from django.db import models
from accounts.models import User

from libs.db.models import DateTimeModel


class VideoModel(DateTimeModel):
    default_file = models.FileField(upload_to='default_video/')
    convert_video = models.FileField(upload_to='convert_video/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')