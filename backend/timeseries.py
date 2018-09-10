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
        sensors = next(reader)[2:]
        units = next(reader)[2:]

        # extract data values
        data = [list(r) for r in zip(*reader)]

        equipments = data[0]
        timestamps = data[1]
        values_list = data[2:]

        unique_equipments = set()

        all_equipment_data = []
        equipment_data = []
        for value_list in values_list:
            data_list = []
            for equipment, timePoint, value in zip(equipments, timestamps, value_list):
                if equipment != '':
                    unique_equipments.add(equipment)
                    data_list.append(equipment_data)
                    equipment_data = []
                    data_point = DataPoint(int(timePoint), float(value))
                    equipment_data.append(data_point)
                else:
                    data_point = DataPoint(int(timePoint), float(value))
                    equipment_data.append(data_point)
            all_equipment_data.append(data_list)

        timeseries_list = []

        for sensor, unit, data in zip(sensors, units, all_equipment_data):
            for e, d in zip(unique_equipments, data):
                timeseries = TimeSeries(e, sensor, unit, d)
                timeseries_list.append(timeseries)

        return timeseries_list, list(unique_equipments), sensors


if __name__ == "__main__":
    ts_list, equipments, sensors = read_data('data2.csv')
    for ts in ts_list:
        print(ts.serialize)
    print(equipments)
    print(sensors)
