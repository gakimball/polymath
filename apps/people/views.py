from apps.people.models import Person
from django.shortcuts import render
from django.template import RequestContext

def about(request):
  data_dict = {}
  return render(request, 'about.html', data_dict)