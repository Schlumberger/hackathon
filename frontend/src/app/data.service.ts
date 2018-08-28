import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';


import { DataPoint } from './data-point.model';
import { DataPointCollectionMeta } from './data-point-collection-meta.model';

@Injectable()
export class DataService {

  constructor(private httpClient: HttpClient) {}

  public getPoints(): Observable<{meta: DataPointCollectionMeta, points: DataPoint[]}> {
    return this.httpClient
     .get('//localhost:5000/timeseries/0', {observe: 'response'})
     .pipe(
       map(response => {
        const responseBody = JSON.parse(response.body.toString());

        const meta: DataPointCollectionMeta = {
          equipment: responseBody.equipment,
          sensor: responseBody.sensor,
          dataPointUnit: responseBody.unit
        };

        const points: DataPoint[] = responseBody.datapoints.map(itemAsString => {
          const item = JSON.parse(itemAsString);
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
