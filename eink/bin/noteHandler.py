#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
from pathlib import Path
import datetime
import json
import shutil

JSON_DIR_PATH = "./json/"
DAILY_TASKS = [
  "zeby",
  "wlosy",
  "prysznic",
  "twarz",
  "spojrzenie w lustro",
  "medytacja 8min",
  "ksiazka 15min",
  "planowanie"
]

WEEKLY_TASKS = {
  "Mon": "Yoga, programowanie",
  "Tue": "Blender, malowanie, 3d",
  "Wen": "Yoga, Security",
  "Thu": "Gaming",
  "Fri": "Yoga, Programowanie",
  "Sat": "Cokolwiek",
  "Sun": "Yoga, muzyka"
  }

def generateMetada(points = 1):
  return {"Done": False, "Points": points}

def createNewJsonDay(day):
  todayJson = {
    "notes": [],
    "previousDays": [],
    "weekly": {"Task": [WEEKLY_TASKS[day]]}.update(generateMetada(10)),
    #"daily": {"Task": DAILY_TASKS, "Done": False, "Points": 1}
    "daily": []
  }
  for dailyTask in DAILY_TASKS:
    todayJson['daily'].append({'Task': dailyTask}.update(generateMetada(1)))
  return todayJson
    
def saveJsonToFile(filePath, jsonData):
  with open(str(filePath), 'w') as jsonFile:
    json.dump(jsonData, jsonFile, indent=2)
  
def main():
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


if __name__ == "__main__":
  main()