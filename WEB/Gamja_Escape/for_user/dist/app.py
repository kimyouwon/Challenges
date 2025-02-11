#!/usr/bin/python3
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    return '살고 싶으면 /error 방향으로 뛰어!!!! 근데... werkzeug가 뭐야?'

@app.route('/error')
def trigger_error():
    raise Exception("Flask Debugger")

@app.route('/<path:file>')
def file(file):
	return open(file).read()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
