from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    # Check if index.html exists, serve it, otherwise show API info
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    
    return jsonify({
        'message': 'Arithmetic API - Version 2.0',
        'endpoints': {
            '/add': 'POST - Add two numbers',
            '/subtraction': 'POST - Subtract two numbers',
            '/multiply': 'POST - Multiply two numbers',
            '/deviser': 'POST - Divide two numbers',
            '/health': 'GET - Health check'
        },
        'example': {
            'url': '/add',
            'method': 'POST',
            'body': {'a': 10, 'b': 5},
            'response': {'result': 15}
        }
    })
SECRET_KEY = "MySuperSecretPassword123"
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    return jsonify({'result': a + b})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    return jsonify({'result': a - b})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    return jsonify({'result': a * b})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 1)
    if b == 0:
        return jsonify({'error': 'Division by zero'}), 400
    return jsonify({'result': a / b})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)