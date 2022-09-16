import requests
import json
url = 'http://127.0.0.1:8000/example/5'
x= requests.get(url=url)
data = x.json()
print(data)      