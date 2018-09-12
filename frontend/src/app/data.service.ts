import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';


import { DataPoint } from './data-point.model';
import { DataPointCollectionMeta } from './data-point-collection-meta.model';

@Injectable()
export class DataService {

  constructor(private httpClient: HttpClient) {}

  public getSensors(deviceId: string): Observable<string[]> {
    return this.httpClient
     .get<string[]>(
       `http://localhost:5000/sensors?deviceid=${deviceId}`, {observe: 'response'})
     .pipe(
       map(response => response.body));
  }

  public getDevices(): Observable<string[]> {
    return this.httpClient
     .get<string[]>(
       `http://localhost:5000/devices`, {observe: 'response'})
     .pipe(
       map(response => response.body));
  }

  public getDataPoints(deviceId: string, sensorId: string): Observable<{meta: DataPointCollectionMeta, points: DataPoint[]}> {
    return this.httpClient
     .get<{equipment, sensor, unit, datapoints}>(
       `http://localhost:5000/timeseries?deviceid=${deviceId}&sensor=${sensorId}`, {observe: 'response'})
     .pipe(
       map(response => {

        const responseBody = response.body;

        const meta: DataPointCollectionMeta = {
          equipment: responseBody.equipment,
          sensor: responseBody.sensor,
          dataPointUnit: responseBody.unit
        };

        const points: DataPoint[] = responseBody.datapoints.map(item => {
            return {
              timestamp: new Date(item['timestamp']).toUTCString(),
              value: item['value']
            };
        });

        return {
          meta,
          points
        };
    }));
  }
}
