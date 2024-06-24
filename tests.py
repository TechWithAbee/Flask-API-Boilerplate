import requests

url = "http://0.0.0.0:8000/api/v0/me"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
