from apps.people.models import Person
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

def about(request):
  people_list = Person.objects.all()
  
  data_dict = {
    'people_list': people_list
  }
  return render(request, 'about.html', data_dict)

def person_detail(request, person_id):
  person = get_object_or_404(Person.objects.prefetch_related('credits'), pk=person_id)

  data_dict = {
    'person': person,
  }

  return render(request, 'people/person_detail.html', data_dict)