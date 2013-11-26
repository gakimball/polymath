from apps.video.models import Video, VideoSeries
from django.shortcuts import render, get_object_or_404

def index(request):
  video_list = Video.objects.only('title', 'image', 'length')

  return render(request, 'video/index.html', {'video_list': video_list})

def video_detail(request, video_id):
  video = get_object_or_404(Video, pk=video_id)
  video_list = Video.objects.only('title', 'image', 'length')

  return render(request, 'video/video_detail.html', {'video': video, 'video_list': video_list})

def outerspaces(request):
  return render(request, 'outerspaces/index.html', {})