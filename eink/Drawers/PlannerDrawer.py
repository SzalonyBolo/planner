#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
import logging
from PIL import Image,ImageDraw,ImageFont
import traceback
import time


def DrawPlanner(jsonData, width, height):
  HBlackimage = Image.new('1', (height, width), 255)
  HRedimage = Image.new('1', (height, width), 255)  # 255: clear the frame
  drawB = ImageDraw.Draw(HBlackimage)
  drawR = ImageDraw.Draw(HRedimage)

  drawNotes(drawB, jsonData)
  drawDaily(drawR, jsonData, width, height)
    
  return HBlackimage, HRedimage

def drawNotes(image, jsonData):
  font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)
  notes = jsonData['notes']
  draw_x = 10
  draw_y = 0
  for note in notes:
    line = note['Task']
    image.text((draw_x, draw_y), line, font = font, fill = 0)
    lineWidth, lineHeight = font.getsize(line)
    draw_y = draw_y + lineHeight

def drawDaily(image, jsonData, width, height):
  font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)
  dailys = jsonData['daily']
  dailysDone = 0
  for daily in dailys:
    if daily['Done']:
      dailysDone = dailysDone + 1
  dailysString = str(dailysDone) + "/" + str(len(dailys))
  image.text((width  - 50, height - 20), dailysString, font = font, fill = 0)