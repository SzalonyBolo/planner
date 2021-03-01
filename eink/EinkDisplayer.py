#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd2in7b
from PIL import Image,ImageDraw,ImageFont
import traceback
import time

class EinkDisplayer:
  
  def __init__(self):
    # import pdb
    # pdb.set_trace()
    self.epd = epd2in7b.EPD()
    self.height = self.epd.height
    self.width = self.epd.width
    self.epd.init()
  #def __del__(self):
    #self.epd.epdconfig.module_exit()

  def displayBlackRedImage(self, Blackimage, Redimage):
    self.epd.Clear()
    time.sleep(1)

    Blackimage = Blackimage.transpose(Image.ROTATE_180)
    Redimage = Redimage.transpose(Image.ROTATE_180)

    self.epd.display(self.epd.getbuffer(Blackimage), self.epd.getbuffer(Redimage))
    time.sleep(2)

    self.epd.sleep()
