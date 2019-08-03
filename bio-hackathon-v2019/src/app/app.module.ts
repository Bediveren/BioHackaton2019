import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ImageUploadComponent } from './image-upload/image-upload.component';
import {MatButtonModule, MatCardModule, MatIconModule} from '@angular/material';
import { MatFileUploadModule } from 'angular-material-fileupload';
import { ResultBlockComponent } from './result-block/result-block.component';
import { CropperComponent } from './cropper/cropper.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import {HttpClientModule} from "@angular/common/http";

@NgModule({
  declarations: [
    AppComponent,
    ImageUploadComponent,
    ResultBlockComponent,
    CropperComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatButtonModule,
    MatFileUploadModule,
    FlexLayoutModule,
    HttpClientModule,
    MatIconModule,
    MatCardModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
