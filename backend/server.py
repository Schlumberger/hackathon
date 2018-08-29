#!/usr/bin/python

from flask import Flask, jsonify, request, Response
from timeseries import TimeSeries, read_data
import json

app = Flask(__name__)

data, equipments, sensors = read_data('data2.csv')


@app.route('/timeseries')
def series():
    espid = request.args.get('espid')
    sensor = request.args.get('sensor')
    for d in data:
        if d.equipment == espid and d.sensor == sensor:
            return jsonify(d.serialize)
    return jsonify("""error""")


@app.route('/sensors')
def sensors():
    return json.dumps(sensors)


@app.route('/devices')
def devices():
    return json.dumps(equipments)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=False)