import requests
from pprint import pprint

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=87778270f2de329e6f7d1f021bdead58&units=metric'.format(city)

#Passing an http request to get data
res = requests.get(url)

data = res.json()

#Retriving data from json
temp = data['main']['temp']
wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

description = data['weather'][0]['description']

pprint('Temprature : {} C'.format(temp))
pprint('Wind Speed : {} m/s'.format(wind_speed))
pprint('Latitude : {}'.format(latitude))
pprint('Longitude : {}'.format(longitude))
pprint('Desc ription : {}'.format(description))
