#!/usr/bin/python

from flask import Flask, jsonify, request
from timeseries import read_data
import json

app = Flask(__name__)

data, equipments, measurements = read_data('data2.csv')


@app.route('/timeseries')
def series():
    espid = request.args.get('espid')
    sensor = request.args.get('sensor')
    for d in data:
        if d.equipment == espid and d.sensor == sensor:
            return d.serialize
    return jsonify("""{error}""")


@app.route('/sensors')
def sensors():
    return json.dumps(measurements)


@app.route('/devices')
def devices():
    return json.dumps(equipments)


@app.after_request
def after_request(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=False)