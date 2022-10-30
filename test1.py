#! python3
"""Module contains python function that checks for weather forecast"""


APPID = 'e789c94cb9a5c2e285c3944fe2cf7027'

import json, requests, sys

#check if the correct argumanets are passed
if len(sys.argv) < 2:
    print   ("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()

location = ' '.join(sys.argv[1:])



url = 'https://api.openweathermap.org/data/2.5/forecast?q=%scnt=3&appid=%s' % (location, APPID)

response = requests.get(url)
response.raise_for_status()

#print(response.text)

weatherData =  json.loads(response.text)

w = weatherData['list']
print(f"\nCurrent weather in {location}: ")
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('The day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
