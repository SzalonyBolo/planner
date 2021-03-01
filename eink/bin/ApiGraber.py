import urllib2
import json

def GetWeather():
  url = "http://wttr.in/Krakow?format=j1"
  opener = urllib2.build_opener()
  opener.addheaders = [('Accept-Language', 'pl')]
  content = opener.open(url).read()
  weather = json.loads(content)
  return weather

