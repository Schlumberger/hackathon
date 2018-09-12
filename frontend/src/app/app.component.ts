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
  public isLoading = true;

  constructor(private dataService: DataService) { }

  public ngOnInit(): void {

    this.dataService.getDevices().subscribe(devices => {
      // get the 1st device for demo purpose
      const device = devices[0];

      this.dataService.getSensors(device).subscribe(sensors => {
        // get the 1st sensor for demo purpose
        const sensor = sensors[0];
        this.updatePoints(device, sensor);
      });
    });
  }

  private updatePoints(device: string, sensor: string) {
    if (!device || !sensor) {
      this.dataPointsMeta = undefined;
      this.dataPoints = undefined;
      return;
    }

    this.dataService.getDataPoints(device, sensor).subscribe(result => {
      this.dataPointsMeta = result.meta;
      this.dataPoints = result.points;
      this.isLoading = false;
    });
  }
}
