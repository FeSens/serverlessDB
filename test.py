from multiprocessing.dummy import Pool

import requests
import uuid
import json

url = "https://ncpiusri49.execute-api.us-east-1.amazonaws.com/dev/"

pool = Pool(10)

def create(arg):
  data = {arg[0]: arg[1]}
  headers = {"Content-Type": "application/json"}
  request = requests.post(url, data=json.dumps(data), headers=headers)
  print(f"{request.json()}, {arg[0]}")

def read(arg):
  headers = {"Content-Type": "application/json"}
  request = requests.get(f"{url}/{arg[0]}", headers=headers)
  print(request.json())

to_be_created = [(uuid.uuid4().hex, uuid.uuid4().hex) for i in range(1000)]

pool.map(create, to_be_created)
pool.map(read, to_be_created)
