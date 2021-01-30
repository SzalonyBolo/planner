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

logging.basicConfig(level=logging.DEBUG)
font12 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)


try:  
    epd = epd2in7b.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)
    
    HBlackimage = Image.new('1', (epd.width, epd.height), 255)
    HRedimage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    drawB = ImageDraw.Draw(HBlackimage)
    drawR = ImageDraw.Draw(HRedimage)
    displayString = "chuju asdf"
    drawB.text((264 - epd.width, 0), displayString, font = font12, fill = 0)
    #epd.display(epd.getbuffer(Himage))
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
    time.sleep(2)
    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    epd2in7.epdconfig.module_exit()
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()
