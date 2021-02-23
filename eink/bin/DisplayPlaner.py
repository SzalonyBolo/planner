#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
import logging
from waveshare_epd import epd2in7b
from PIL import Image,ImageDraw,ImageFont
import traceback
import time


class DisplayPlaner:
  
  def __init__(self):
    self.epd = epd2in7b.EPD()
    logging.info("init and Clear")
    self.font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)

  def displayPlaner(self, jsonData):
    HBlackimage = Image.new('1', (self.epd.height, self.epd.width), 255)
    HRedimage = Image.new('1', (self.epd.height, self.epd.width), 255)  # 255: clear the frame
    drawB = ImageDraw.Draw(HBlackimage)
    drawR = ImageDraw.Draw(HRedimage)

    self.drawNotes(drawB, jsonData)
    self.drawDaily(drawR, jsonData)

    HBlackimage = HBlackimage.transpose(Image.ROTATE_180)
    HRedimage = HRedimage.transpose(Image.ROTATE_180)

    logging.info("init and Clear")
    self.epd.init()
    self.epd.Clear()
    time.sleep(1)

    self.epd.display(self.epd.getbuffer(HBlackimage), self.epd.getbuffer(HRedimage))
    time.sleep(2)

    logging.info("Goto Sleep...")
    self.epd.sleep()

  def drawNotes(self, image, jsonData):
    notes = jsonData['notes']
    draw_x = 10
    draw_y = 0
    for note in notes:
      line = note['Task']
      image.text((draw_x, draw_y), line, font = self.font, fill = 0)
      width, height = self.font.getsize(line)
      draw_y = draw_y + height

  def drawDaily(self, image, jsonData):
    dailys = jsonData['daily']
    dailysDone = 0
    for daily in dailys:
      if daily['Done']:
        dailysDone = dailysDone + 1
    dailysString = str(dailysDone) + "/" + str(len(dailys))
    image.text((self.epd.width  - 50, self.epd.height - 20), dailysString, font = self.font, fill = 0)