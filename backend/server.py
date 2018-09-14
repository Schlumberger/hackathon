#!/usr/bin/python

from flask import Flask, jsonify, request, abort
from timeseries import read_data
import json

app = Flask(__name__)

data, equipments, sensors_per_equipment = read_data('dataset/data-large.csv')


@app.route('/timeseries')
def series():
    device_id = request.args.get('deviceid')
    sensor = request.args.get('sensor')
    for d in data:
        if d.equipment == device_id and d.sensor == sensor:
            return d.serialize
    abort(404)


@app.route('/sensors')
def sensors():
    device_id = request.args.get('deviceid')
    if(device_id in sensors_per_equipment):
        return json.dumps(sensors_per_equipment[device_id])
    abort(404)


@app.route('/devices')
def devices():
    return json.dumps(equipments)


@app.after_request
def after_request(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=False)
