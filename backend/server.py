#!/usr/bin/python

from flask import Flask, jsonify
from timeseries import TimeSeries, DataPoint, read_data

app = Flask(__name__)

data = read_data('data.csv')

@app.route('/timeseries/<int:id>')
def series(id):
    ts = data[id]
    return jsonify(ts.serialize)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)