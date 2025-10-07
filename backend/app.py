from flask import Flask, request, jsonify
import json, os, joblib

app = Flask(__name__)
DATA_FILE = 'data.json'
MODEL_FILE = 'outbreak_model.pkl'

# Placeholder: create JSON if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/submit_health_data', methods=['POST'])
def submit_health_data():
    data = request.json
    with open(DATA_FILE, 'r') as f:
        existing = json.load(f)
    existing.append(data)
    with open(DATA_FILE, 'w') as f:
        json.dump(existing, f, indent=2)
    return jsonify({'status':'success'})

@app.route('/get_predictions', methods=['GET'])
def get_predictions():
    return jsonify({'risk':'Low (placeholder)'})

if __name__ == '__main__':
    app.run(debug=True)
