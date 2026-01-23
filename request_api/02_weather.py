from pprint import pprint
import requests

# 서울 위/경도
lat = 37.56
lon = 126.97
api_key = '17a09334ee4793f86a0c7c9cc14fc7e2'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

response = requests.get(url).json()

pprint(response)