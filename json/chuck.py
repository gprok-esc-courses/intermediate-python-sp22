import requests
import json

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)

print(response.text)
data = json.loads(response.text)

print(data)

print(data['value'])

