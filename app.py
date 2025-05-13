from flask import Flask, request, jsonify
from google.cloud import datastore

app = Flask(__name__)
datastore_client = datastore.Client()

@app.route('/')
def home():
    return 'App Engine with Custom Runtime & Datastore Working!'

@app.route('/add', methods=['POST'])
def add_entity():
    data = request.json
    entity = datastore.Entity(key=datastore_client.key('Task'))
    entity.update({
        'description': data.get('description')
    })
    datastore_client.put(entity)
    return jsonify({'message': 'Entity added'}), 200

@app.route('/list', methods=['GET'])
def list_entities():
    query = datastore_client.query(kind='Task')
    tasks = list(query.fetch())
    return jsonify(tasks), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
