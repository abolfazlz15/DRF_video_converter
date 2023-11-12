from django.urls import path
from video.api import views



urlpatterns = [
    path('convert/', views.VideoUploadConvertView.as_view(), name='convert_video'),
    path('list/<int:id>/', views.UserVideoListView.as_view(), name='video_list'),
]