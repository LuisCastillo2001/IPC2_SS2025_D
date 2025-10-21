from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime

# Simple config (cambiar SECRET_KEY en producción)
SECRET_KEY = "A"

USERS = {
    "Luis": "123"  # usuario de ejemplo
}

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'msg': 'username and password required'}), 400
    if USERS.get(username) != password:
        return jsonify({'msg': 'invalid credentials'}), 401

    payload = {
        'sub': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return jsonify({'access_token': token})

@app.route('/protected', methods=['GET'])
def protected():
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return jsonify({'msg': 'missing authorization header'}), 401
    token = auth.split(' ', 1)[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'msg': f'Hello {payload["sub"]}', 'user': payload['sub']})
    except jwt.ExpiredSignatureError:
        return jsonify({'msg': 'token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'msg': 'invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True)