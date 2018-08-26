"""
Time series
"""

import csv
import json


class DataPoint():
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value


class TimeSeries():
    def __init__(self, equipment, sensor, unit, data):
        self.equipment = equipment
        self.sensor = sensor
        self.unit = unit
        self.data = data

    @property
    def serialize(self):
        return json.dumps(self.__dict__)

def read_data(data_file):
    with open(data_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=',')
        equipments = next(reader)
        sensors = next(reader)
        units = next(reader)
        data = [list(r) for r in zip(*reader)]

        timeseries_list = []

        for e, s, u, d in zip(equipments, sensors, units, data):
            ts = TimeSeries(e, s, u, d)
            timeseries_list.append(ts)

        return timeseries_list

if __name__ == "__main__":
    ts_list = read_data('data.csv')
    for ts in ts_list:
        print(ts.serialize)
