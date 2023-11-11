from django.urls import path
from video.api import views
from rest_framework import routers



urlpatterns = [
    path('convert/', views.VideoUploadConvertView.as_view(), name='convert_video'),
]