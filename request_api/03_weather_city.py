import requests
from pprint import pprint

city_name = "Seoul,KR"
api_key = '17a09334ee4793f86a0c7c9cc14fc7e2'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

response = requests.get(url).json()
pprint(response)