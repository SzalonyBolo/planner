import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'eink/lib')
bindir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'eink/bin')
sys.path.append(libdir)
sys.path.append(bindir)
#from waveshare_epd import epd2in7b
from weather import display_weather
from pathlib import Path
import datetime
import json

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