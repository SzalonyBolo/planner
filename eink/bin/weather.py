#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
import os
import sys
from pathlib import Path
import json
from PIL import Image,ImageDraw,ImageFont

pngdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'wpng')
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
  sys.path.append(libdir)
from waveshare_epd import epd2in7b

def display_weather(c):
  #get data
  # url = "http://wttr.in/Krakow?format=j1"
  # req = Request(url)
  # req.add_header('Accept-Language', 'pl')
  # content = urlopen(req).read()
  # c = json.loads(content)

  #data mock
  # modulePath = os.path.dirname(os.path.abspath('weather.py'))
  # mockPath = os.path.join(modulePath, 'Krakow.json')
  # with open(mockPath) as file:
  # c = json.load(file)

  current = c.get('current_condition')[0]
  FeelsLike = [current['FeelsLikeC']]
  Temp = [current['temp_C']]
  Humidity = [current['humidity']]
  Time = [current['observation_time']]
  Pressure = [current['pressure']]
  PrecipMM = [current['precipMM']]
  Clouds = [current['cloudcover']]
  Wind = [current['windspeedKmph']]

  tommorow = c.get('weather')[1]['hourly'][4]
  FeelsLike.append(tommorow['FeelsLikeC'])
  Temp.append(tommorow['tempC'])
  Humidity.append(tommorow['humidity'])
  Pressure.append(tommorow['pressure'])
  PrecipMM.append(tommorow['precipMM'])
  Clouds.append(tommorow['cloudcover'])
  Wind.append(tommorow['windspeedKmph'])

  aftertommorow = c.get('weather')[2]['hourly'][4]
  FeelsLike.append(aftertommorow['FeelsLikeC'])
  Temp.append(aftertommorow['tempC'])
  Humidity.append(aftertommorow['humidity'])
  Pressure.append(aftertommorow['pressure'])
  PrecipMM.append(aftertommorow['precipMM'])
  Clouds.append(aftertommorow['cloudcover'])
  Wind.append(aftertommorow['windspeedKmph'])

  iconsheights = [13, 35, 58, 70, 87, 106]
  headerwidths = [20, 105, 175]
  textwidths = [33, 115, 200]
  textheights = [20, 36, 54, 71, 88, 105]

  font12 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 12)
  font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)

  epd = epd2in7b.EPD()

  Bimage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
  Rimage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame

  rdraw = ImageDraw.Draw(Rimage)
  #Headers
  rdraw.text((headerwidths[0], 0), "Teraz" , font = font18, fill = 0)
  rdraw.text((headerwidths[1], 0), "Jutro" , font = font18, fill = 0)
  rdraw.text((headerwidths[2], 0), "Pojutrze" , font = font18, fill = 0)

  #icons
  termbmp = Image.open(os.path.join(pngdir, 'thermometer_crop.bmp'))
  Rimage.paste(termbmp, (2,iconsheights[0]))

  rainbmp = Image.open(os.path.join(pngdir, 'rain.bmp'))
  Rimage.paste(rainbmp, (0,iconsheights[1]))

  windbmp = Image.open(os.path.join(pngdir, 'wind.bmp'))
  Rimage.paste(windbmp, (0,iconsheights[2]))

  cloudbmp = Image.open(os.path.join(pngdir, 'clouds.bmp'))
  Rimage.paste(cloudbmp, (0,iconsheights[3]))

  humbmp = Image.open(os.path.join(pngdir, 'hum_crop.bmp'))
  Rimage.paste(humbmp, (0,iconsheights[4]))

  barbmp = Image.open(os.path.join(pngdir, 'barometr_crop.bmp'))
  Rimage.paste(barbmp, (0,iconsheights[5]))

  draw = ImageDraw.Draw(Bimage)
  for i in range(0,3):
    draw.text((textwidths[i], textheights[0]), str(Temp[i]) + "°/".decode('utf-8') + str(FeelsLike[0]) + "° C".decode('utf-8'), font = font12, fill = 0)
    draw.text((textwidths[i], textheights[1]), str(PrecipMM[i]) + "mm", font = font12, fill = 0)
    draw.text((textwidths[i], textheights[2]), str(Wind[i]) + "kmph", font = font12, fill = 0)
    draw.text((textwidths[i], textheights[3]), str(Clouds[i]) + "%", font = font12, fill = 0)
    draw.text((textwidths[i], textheights[4]), str(Humidity[i]) + "%", font = font12, fill = 0)
    draw.text((textwidths[i] - 7, textheights[5]), str(Pressure[i]) + "hPa", font = font12, fill = 0)

  draw.line((0, 127, epd.height, 127), fill = 0)

  try:  
    epd.init()
    #epd.Clear(0xFF) #epd2in7
    epd.Clear() #epd2in7b

    #epd.display(epd.getbuffer(Bimage)) #epd2in7
    epd.display(epd.getbuffer(Bimage), epd.getbuffer(Rimage)) #epd2in7b

    epd.sleep()

    

  except IOError as e:
      #logging.info(e)
      epd2in7b.epdconfig.module_exit()

  except KeyboardInterrupt:    
      #logging.info("ctrl + c:")
      epd2in7b.epdconfig.module_exit()
      #exit()