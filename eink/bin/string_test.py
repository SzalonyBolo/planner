#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import textwrap
import unicodedata
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

SCREEN_WIDTH = 264
SCREEN_HEIGHT = 176

logging.basicConfig(level=logging.DEBUG)

displayString = u"o chuj chodzi z tymi" 

try:
    epd = epd2in7.EPD()
    
    '''2Gray(Black and white) display'''
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    fonts = []
    sizes = []
    for i in reversed(range(13)):
        fonts.append(ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), i))
        sizes.append(i)
    # Drawing on the Horizontal image
    # resolution 264x176
    # font size 8 - lowest readable
    # u"✔ ✓ √"  - working
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    
    #logging.info(width)
    #logging.info(height)
    #draw.text((264 - width, 0), displayString, font = font12, fill = 0)
    hpos = 0
    for i in range(13):
        width, height = draw.textsize(displayString, font=fonts[i])
        draw.text((10, hpos), displayString + " " + str(sizes[i]) + u"☐ ☑ ☒", font = fonts[i], fill = 0)
        hpos = hpos + height
    epd.display(epd.getbuffer(Himage))
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
