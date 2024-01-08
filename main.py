from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"foo": 2})

if __name__ == '__main__':
    app.run()
