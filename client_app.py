from flask import Flask, send_file, jsonify, request
import os
import sys
import json

def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = Flask(__name__)

# Load config
CONFIG_FILE = "server_config.json"
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"API_URL": "http://localhost:8000"}

@app.route('/')
@app.route('/index.html')
def serve_index():
    return send_file(get_resource_path('index.html'))

@app.route('/config')
def get_config():
    return jsonify(load_config())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=False)
