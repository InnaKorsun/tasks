import http.client
import requests
import json

url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.text)
print(r.headers)

payload = {'key1': 'value1'}
r = requests.get(url, params=payload)
print(r.url)
print(r.text)

a =json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(a)
b = r.json()
print(b)
