import { Component, OnInit } from '@angular/core';
import {CellCounterService} from "../cell-counter.service";

@Component({
  selector: 'app-image-upload',
  templateUrl: './image-upload.component.html',
  styleUrls: ['./image-upload.component.css']
})
export class ImageUploadComponent implements OnInit {

  constructor(private cellCounter: CellCounterService) { }

  ngOnInit() {
  }

  public imagePath;
  imgURL: string | ArrayBuffer | null = "assets/logo.png";
  public message: string;
  public image: File;

  preview(files) {
    if (files.length === 0)
      return;

    let mimeType = files[0].type;
    if (mimeType.match(/image\/*/) == null) {
      this.message = "Only images are supported.";
      return;
    }

    let reader = new FileReader();
    this.imagePath = files;
    reader.readAsDataURL(files[0]);
    reader.onload = (_event) => {
      this.imgURL = reader.result;
      this.image = files[0];
    }
  }

  onUpload() {
    this.cellCounter.count(this.image).subscribe(event => {
      console.log(event);
    })
  }
}
