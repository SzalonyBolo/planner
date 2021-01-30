# -*- coding: utf-8 -*-
# try something like
def index(): 
  return dict(message="hello from display.py")

def weather():
  import urllib2
  import json
  url = "http://wttr.in/Krakow?format=j1"
  opener = urllib2.build_opener()
  opener.addheaders = [('Accept-Language', 'pl')]
  content = opener.open(url).read()
  c = json.loads(content)
  display_weather(c)
  return dict()

def notes():
  import datetime
  import pdb
  import os
  from pathlib import Path
  pdb.set_trace()
  todayDate = datetime.date.today()
  today = todayDate.strftime("%d.%m.%y")

  todayJson = {}
  todayJsonPathFile = Path(JSON_DIR_PATH + today + '.json')
  if not todayJsonPathFile.is_file(): 
    todayJson = createNewJsonDay(todayDate.strftime("%a"))
  else:
    with open(str(todayJsonPathFile), 'r') as todayNote:
      todayJson = json.loads(todayNote.read())

  todayTaskPath = Path('./notes/' + today)
  if todayTaskPath.is_file():
    with open(str(todayTaskPath), 'r') as todayTasksFile:
      tasksFromFile = todayTasksFile.readlines()
      for fileTask in tasksFromFile:
        todayJson['notes'].append({'Task': fileTask}.update(generateMetada(10)))
      json.dump(todayJsonPathFile, todayJson)

  return "dict()"