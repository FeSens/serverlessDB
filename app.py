from flask import Flask, request, jsonify
import dbm
import os
app = Flask(__name__)

db_path = os.environ.get('DB_PATH')

@app.route("/", methods=['GET'])
def index():
  with dbm.open(db_path, 'ru') as db:
    keys = db.keys()
  
  return jsonify(keys=[k.decode("utf-8") for k in keys])

@app.route("/<key>")
def show(key):
  with dbm.open(db_path, 'ru') as db:
    data = db.get(key)

  if data:
    return jsonify(value=data.decode("utf-8") )
  
  return jsonify(error="No Value Found")

@app.route("/", methods=['POST'])
def create():
  data = request.json
  while True:
    try:
      with dbm.open(db_path, 'c') as db:
        for k, v in data.items():
          db[k] = v

      return jsonify(message="success")
    
    except Exception as e:
      pass
      #return jsonify(error=str(e))

@app.route("/<key>", methods=['DELETE'])
def destroy(key):
  with dbm.open(db_path, 'c') as db:
      del db[key]

  return jsonify(message="success")