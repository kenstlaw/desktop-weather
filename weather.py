#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import requests
import json
from configparser import ConfigParser

parser = ConfigParser()
parser.read('desktop_weather.ini')

apikey = parser.get('Weather_Desktop','apikey')
coords = parser.get('Weather_Desktop','coord')

WeatherUrl = "https://api.darksky.net/forecast/" + apikey + "/" + coords 


WeatherRequests = requests.get(WeatherUrl,timeout=1.0)

WeatherResponse = json.loads(WeatherRequests.text)

CurrentWeather = WeatherResponse['currently']

Humidity = CurrentWeather['humidity'] * 100


print ("Current Tempeture    : %3.0fF"% CurrentWeather['temperature'])
print ("Dew Point            : %3.0fF"% CurrentWeather['dewPoint'])
print ("Current Humidity     : %3.0f%%"% Humidity)
print ("Corrent Conditions   :", CurrentWeather['summary'])

exit(0)
