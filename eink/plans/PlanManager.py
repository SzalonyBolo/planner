# -*- coding: utf-8 -*-
# try something like
 import datetime
import os
from pathlib import Path
import DisplayPlaner

todayDate = datetime.date.today()
today = todayDate.strftime("%d.%m.%y")
todayJson = getTodayJson(todayDate)

todayTaskPath = TASKS_DIR.joinpath(today)
if todayTaskPath.is_file():
  with open(str(todayTaskPath), 'r') as todayTasksFile:
    tasksFromFile = todayTasksFile.readlines()
  for fileTask in tasksFromFile:
    jsonTask = generateTaskFromNote(fileTask)
    todayJson['notes'].append(jsonTask)
