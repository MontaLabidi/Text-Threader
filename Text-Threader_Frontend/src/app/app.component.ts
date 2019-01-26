import { Component, ViewChild } from '@angular/core';
import { UploadService } from './upload/Upload.service';
import { forkJoin } from 'rxjs';
import { MatDialog } from '@angular/material';
import { DialogComponent } from './upload/dialog/dialog.component';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {}
  
