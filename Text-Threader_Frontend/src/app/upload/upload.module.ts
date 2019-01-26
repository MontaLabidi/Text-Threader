import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UploadComponent } from './upload.component';
import { MatButtonModule, MatDialogModule, MatListModule, MatProgressBarModule, MatTabsModule, MatIconModule, MatInputModule } from '@angular/material';
import { DialogComponent } from './dialog/dialog.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';
import { UploadService } from './upload.service';
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from '../app-routing.module';

@NgModule({
  imports: [CommonModule,
            MatButtonModule,
            MatDialogModule,
            MatListModule,
            FlexLayoutModule,
            HttpClientModule,
            MatProgressBarModule,
            BrowserModule,
            AppRoutingModule,
            BrowserAnimationsModule,
            MatTabsModule,
            MatIconModule,
            MatInputModule
          ],
  declarations: [UploadComponent, DialogComponent],
  exports: [UploadComponent],
  entryComponents: [DialogComponent,UploadComponent], // Add the DialogComponent as entry component
  providers: [UploadService]
})
export class UploadModule {}
