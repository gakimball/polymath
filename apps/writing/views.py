from apps.writing.models import Story, Collection
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import Http404

def index(request):
  story_list = Story.objects.all()

  data_dict = {
    'story_list': story_list
  }

  return render(request, 'writing/index.html', data_dict)

def story_detail(request, story_id):
  story = get_object_or_404(Story, pk=story_id)

  data_dict = {
    'story': story
  }

  return render(request, 'writing/story_detail.html', data_dict)

def zine_index(request):
  return render(request, 'writing/zine_index.html')