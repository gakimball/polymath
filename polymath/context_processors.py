import os
import re

# Determines what dept. the user is currently in and creates a new context variable
def current_dept(request):
  music = '/(music|tracks|releases|artists)'
  video = '/video'
  writing = '/(writing|read|zine)'
  os = '/(theouterspaces)'

  current_dept = 'na'
  if re.match(music, request.path) is not None:
    current_dept = 'music'
  if re.match(video, request.path) is not None:
    current_dept = 'video'
  if re.match(writing, request.path) is not None:
    current_dept = 'writing'
  if re.match(os, request.path) is not None:
    current_dept = 'os'

  return {'current_dept': current_dept, 'current_dept_index': 'apps.' + current_dept.lower() + '.views.index'}

def is_debug(request):
  is_debug = True if os.environ.get('DJANGO_DEBUG', None) == '1' else False
  return { 'is_debug': is_debug, }