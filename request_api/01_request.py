import requests
from pprint import pprint

url = "https://fakestoreapi.com/carts"

# API 요청 보내기
response = requests.get(url).json()
# json() -> json 타입을 딕셔너리로 변환해주는 함수

pprint(response)