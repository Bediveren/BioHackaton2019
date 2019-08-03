import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-cropper',
  templateUrl: './cropper.component.html',
  styleUrls: ['./cropper.component.css']
})
export class CropperComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  @Input()
  imgURL: any;

}
