from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run()
