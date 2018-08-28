#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import requests
import json


WeatherUrl = "https://api.darksky.net/forecast/[api key]/42.568946,-71.265706"

WeatherRequests = requests.get(WeatherUrl,timeout=1.0)

#print WeatherRequests.text
WeatherResponse = json.loads(WeatherRequests.text)

#print type(WeatherResponse)

#for key in WeatherResponse:
#   print key

#print type(WeatherResponse['currently'])

#for key in WeatherResponse['currently']:
#   print key
CurrentWeather = WeatherResponse['currently']


Humidity = CurrentWeather['humidity'] * 100


print ("Current Tempeture    : %3.0fF"% CurrentWeather['temperature'])
print ("Dew Point            : %3.0fF"% CurrentWeather['dewPoint'])
print ("Current Humidity     : %3.0f%%"% Humidity)
print ("Corrent Conditions   :", CurrentWeather['summary'])
