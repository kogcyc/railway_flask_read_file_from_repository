from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/')
def index():
    r.set('foo', 'bar')
    rett = r.get('foo')
    return jsonify({"foo": ret})

if __name__ == '__main__':
    app.run()
