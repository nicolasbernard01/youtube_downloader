from pytube import YouTube 
from django.shortcuts import render, HttpResponse, redirect
import os


def index(request):

    return render(request, 'downloader/index.html', None)

def video_downloader(request):

    urlv = ''

    if request.method == 'POST':

        try:

            urlv = request.POST['urlv']

            ytv = YouTube(urlv).streams.get_highest_resolution().download()

            with open(ytv, 'rb') as video:

                response = HttpResponse(video.read())

            response['Content-Type'] = 'Video'

            video_name = os.path.basename(ytv)

            response['Content-Disposition'] = f'attachment; filename="{video_name}"'

            os.remove(ytv)

            return response

        except:

            redirect('video_downloader.html')

    return render(request, 'downloader/video_downloader.html', None)

        
def audio_downloader(request):

    urla = ''

    try:

        if request.method == 'POST':

            urla = request.POST['urla']

            yta = YouTube(urla).streams.filter(only_audio=True).first().download()

            with open(yta, 'rb') as audio:

                response = HttpResponse(audio.read())

            response['Content-Type'] = 'Audio'

            audio_name = os.path.basename(yta)

            response['Content-Disposition'] = f'attachment; filename="{audio_name}"'

            os.remove(yta)

            return response

    except:

        redirect('audio_downloader.html')

    return render(request, 'downloader/audio_downloader.html', None)

   