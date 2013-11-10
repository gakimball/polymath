from django import template

register = template.Library()

@register.filter
def next(value, arg):
  try:
    return value[int(arg)-1]
  except:
    return None