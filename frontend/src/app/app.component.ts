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
  public itemsMeta: DataPointCollectionMeta;
  public items: DataPoint[];

  constructor(private dataService: DataService) {}

  public ngOnInit(): void {
    this.dataService.getPoints().subscribe(result => {
      this.itemsMeta = result.meta;
      this.items = result.points;
    });
  }
}
