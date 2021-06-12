import requests
from pprint import pprint

#this part creates the variables for the key and the api's website used
API_key = '176891421c95b26f591465564823f992'
url = f'https://api.openweathermap.org/data/2.5/weather?q=Yaounde&appid={API_key}'

#this part asks for request from the api to get all the information availabel there
content = requests.get(url).json()
pprint(content)
content_main = content['main']
weather = content['weather'][0]
wind = content['wind']

#this collects temperature, humidity, precipitation and wind information
min_temp = content_main['temp_min']
max_temp = content_main['temp_max']
humidity = content_main['humidity']
precipitation = weather['main']
precipitation_description = weather['description']
wind_direction = wind['deg']
wind_speed = wind['speed']

average_temp = ((min_temp+max_temp)/2)-273.15

#then it finally arranges the information in an orderly and easy to read manner
dict_of_important_values = {'average_temp': average_temp, 'humidity': humidity, 'weather': {'weather_condition': precipitation,
                                                                                            'weather_intensity': precipitation_description}, 'wind': {'wind_direction': wind_direction, 'wind_speed': wind_speed}}

pprint(dict_of_important_values)
