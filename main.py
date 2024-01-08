from flask import Flask, jsonify
import os

app = Flask(__name__)

fp = open('data','r')
datta = fp.read()
fp.close()

@app.route('/')
def index():
    return jsonify({"foo": datta})

if __name__ == '__main__':
    app.run()
