"""
Time series
"""

import csv
import json


class DataPoint():
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value

    @property
    def serialize(self):
        return self.__dict__


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
    with open(data_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        
        # extract metadata
        equipments = next(reader)[1:]
        sensors = next(reader)[1:]
        units = next(reader)[1:]

        sensors_per_equipment = {}
        
        for i in range(len(equipments)):
            if(equipments[i] in sensors_per_equipment):
                sensors_per_equipment[equipments[i]].append(sensors[i])
            else:
                sensors_per_equipment[equipments[i]] = []
                sensors_per_equipment[equipments[i]].append(sensors[i])

        # extract data values
        data = [list(r) for r in zip(*reader)]

        timestamps = data[0]
        values_list = data[1:]

        datapoints_list = []
        for values in values_list:
            datapoints = [DataPoint(int(t), float(v)) for t, v in zip(timestamps, values)]
            datapoints_list.append(datapoints)

        timeseries_list = []

        for e, s, u, dp in zip(equipments, sensors, units, datapoints_list):
            ts = TimeSeries(e, s, u, dp)
            timeseries_list.append(ts)

        return timeseries_list, list(set(equipments)),sensors_per_equipment


if __name__ == "__main__":
    ts_list, equipments, sensors_per_equipment = read_data('input/data-small.csv')
    # for ts in ts_list:
    #     print(ts.serialize)
    # print(equipments)
    # print(sensors)
