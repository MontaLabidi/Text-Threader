import { Component } from '@angular/core';
import { MatDialog } from '@angular/material';
import { DialogComponent } from './dialog/dialog.component';
import { UploadService } from './upload.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent {
  constructor(public dialog: MatDialog, public uploadService: UploadService) {}
  Language;
  Sentiment;
  result;
  public predict(sentance:string){

  this.result=this.uploadService.predict(sentance).subscribe(data => {
    console.log(data);
  this.Language=data["Language"];
  this.Sentiment=data["Sentiment"]});

}
  public openUploadDialog() {
    let dialogRef = this.dialog.open(DialogComponent, { width: '70%', height: '70%' });
  }
}
