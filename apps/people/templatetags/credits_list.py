from django import template
from apps.people.models import Credit
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.inclusion_tag('people/credits_list.html', takes_context=True)
def credits_list(context, item):
  content_type = ContentType.objects.get_for_model(item)
  object_id    = item.id

  credits_list = Credit.objects.filter(content_type=content_type, object_id=object_id).order_by('person').prefetch_related('person')

  return {
  'credits_list': credits_list,
  }