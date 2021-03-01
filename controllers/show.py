# -*- coding: utf-8 -*-

def index():
  return dict(message="hello from display.py")

def weather():
  from bin.ApiGraber import GetWeather
  from Drawers.WeatherDrawer import DrawWeather
  weather = GetWeather()
  Bimg, Rimg = DrawWeather(weather, Displayer.width, Displayer.height)
  Displayer.displayBlackRedImage(Bimg, Rimg)
  return "pogoda"

def planner():
  from Drawers.PlannerDrawer import DrawPlanner
  from bin.NoteHandler import GetAndUpdatePlans
  todayJson = GetAndUpdatePlans()
  BImg, RImg = DrawPlanner(todayJson, Displayer.width, Displayer.height)
  Displayer.displayBlackRedImage(BImg, RImg)
  return "hehe"

