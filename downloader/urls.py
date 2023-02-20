
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name='index'),
    path('video_downloader', views.video_downloader, name='video_downloader'),
    path('audio_downloader', views.audio_downloader, name='audio_downloader'),
    
]