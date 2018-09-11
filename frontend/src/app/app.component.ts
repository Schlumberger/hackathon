import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';
import { DataPoint } from './data-point.model';
import { DataPointCollectionMeta } from './data-point-collection-meta.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  public title = 'Schlumberger Hackathon Challenge';
  public dataPointsMeta: DataPointCollectionMeta;
  public dataPoints: DataPoint[];
  public sensors: string[];
  public devices: string[];

  constructor(private dataService: DataService) {}

  public ngOnInit(): void {
    this.dataService.getSensors().subscribe(sensors => {
      this.sensors = sensors;
      this.updatePoints();
    });

    this.dataService.getDevices().subscribe(devices => {
      this.devices = devices;
      this.updatePoints();
    });
  }

  private updatePoints() {
    if (
      !this.sensors ||
      this.sensors.length < 1 ||
      !this.devices ||
      this.devices.length < 1) {
        this.dataPointsMeta = undefined;
        this.dataPoints = undefined;
        return;
      }

    this.dataService.getDataPoints(this.devices[0], this.sensors[1]).subscribe(result => {
      this.dataPointsMeta = result.meta;
      this.dataPoints = result.points;
    });
  }
}
