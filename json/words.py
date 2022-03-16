import requests
import json

url = 'https://random-word-api.herokuapp.com/word?number=1'
response = requests.get(url)

print(response.text)
data = json.loads(response.text)

print(data[0])