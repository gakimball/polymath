import re

# Determines what dept. the user is currently in and creates a new context variable
def current_dept(request):
  music = '/(music|tracks|artists)'
  video = '/video'
  writing = '/(writing|story)'

  current_dept = 'na'
  if re.match(music, request.path) is not None:
    current_dept = 'music'
  if re.match(video, request.path) is not None:
    current_dept = 'video'
  if re.match(writing, request.path) is not None:
    current_dept = 'writing'

  return {'current_dept': current_dept, 'current_dept_index': 'apps.' + current_dept.lower() + '.views.index'}