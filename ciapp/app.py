import os
from flask import Flask, jsonify, request

app = Flask(__name__)


def add(a, b):
    return a + b


@app.get("/")
def index():
    return jsonify(message="Hello from the Skillsforge CI demo")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/add")
def add_endpoint():
    try:
        a = float(request.args["a"])
        b = float(request.args["b"])
    except (KeyError, ValueError):
        return jsonify(error="send numbers as ?a=1&b=2"), 400
    return jsonify(result=add(a, b))
