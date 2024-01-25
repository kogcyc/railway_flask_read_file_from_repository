from flask import Flask, jsonify

app = Flask(__name__)

with open('data','r') as fp:
    valu = fp.read()

@app.route('/')
def index():
    return jsonify({"key": valu})

if __name__ == '__main__':
    app.run()
