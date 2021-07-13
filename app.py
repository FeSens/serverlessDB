from flask import Flask, request, jsonify
import dbm
import os
app = Flask(__name__)

db_path = os.environ.get('DB_PATH')

@app.route("/", methods=['GET'])
def index():
  with dbm.open(db_path, 'r') as db:
    keys = db.keys()
  
  return jsonify(keys=[k.decode("utf-8") for k in keys])

@app.route("/<key>")
def show(key):
  with dbm.open(db_path, 'r') as db:
    data = db.get(key).decode("utf-8") 

  return jsonify(value=data)

@app.route("/", methods=['POST'])
def create():
  data = request.json
  print(data)
  with dbm.open(db_path, 'c') as db:
    for k, v in data.items():
      print(k, v)
      db[k] = v
  
  return jsonify(message="success")

@app.route("/<key>", methods=['DELETE'])
def destroy(key):
  with dbm.open(db_path, 'c') as db:
      del db[key]

  return jsonify(message="success")