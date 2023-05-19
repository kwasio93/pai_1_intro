import requests

url = "https://httpbin.org/post"
headers = {'Content-Type': 'application/json',"Content-Length": "0"}
data = {'imie':'natalia'}
files = {'plik':'json.txt'}
response = requests.post(url, headers=headers, json=data)
print(response.text)
