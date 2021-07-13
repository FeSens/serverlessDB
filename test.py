import requests
import uuid
import json

url = "https://ncpiusri49.execute-api.us-east-1.amazonaws.com/dev/"

keys = []
for i in range(10):
  data = { uuid.uuid4().hex: uuid.uuid4().hex}

  keys += data.keys()
  headers = {"Content-Type": "application/json"}
  request = requests.post(url, data=json.dumps(data), headers=headers)
  print(request)

for i in keys:
  headers = {"Content-Type": "application/json"}
  request = requests.get(f"{url}/{i}", headers=headers)
  print(request.json())