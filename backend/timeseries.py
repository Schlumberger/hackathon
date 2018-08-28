"""
Time series
"""

import csv
import json
import datetime
import time


class DataPoint():
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value

    @property
    def serialize(self):
        return json.dumps(self.__dict__, cls=ComplexEncoder)


class TimeSeries():
    def __init__(self, equipment, sensor, unit, datapoints):
        self.equipment = equipment
        self.sensor = sensor
        self.unit = unit
        self.datapoints = datapoints

    @property
    def serialize(self):
        return json.dumps(self.__dict__, cls=ComplexEncoder)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DataPoint) or isinstance(obj, TimeSeries):
            return obj.serialize
        else:
            return json.JSONEncoder.default(self, obj)

def read_data(data_file):
    with open(data_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=',')
        
        # extract metadata
        equipments = next(reader)[1:]
        sensors = next(reader)[1:]
        units = next(reader)[1:]

        # extract data values
        data = [list(r) for r in zip(*reader)]

        # 1st column are timestamps
        timestamps = data[0]
        # Remaining columns are values 
        values_list = data[1:]

        datapoints_list = []
        for values in values_list:
            datapoints = [DataPoint(int(t), float(v)) for t, v in zip(timestamps, values)]
            #datapoints = [(t,v) for t, v in zip(timestamps, values)]
            datapoints_list.append(datapoints)

        timeseries_list = []

        for e, s, u, dp in zip(equipments, sensors, units, datapoints_list):
            ts = TimeSeries(e, s, u, dp)
            timeseries_list.append(ts)

        return timeseries_list


if __name__ == "__main__":
    ts_list = read_data('data.csv')
    for ts in ts_list:
        print(ts.serialize)
