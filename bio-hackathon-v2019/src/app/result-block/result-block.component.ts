import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-result-block',
  templateUrl: './result-block.component.html',
  styleUrls: ['./result-block.component.css']
})
export class ResultBlockComponent implements OnInit {

  constructor() {
  }

  ngOnInit() {
    let split = this.totalCells.toExponential(5).split("e+");
    this.part = split[0].replace(/(\.[0-9]*[1-9])0+$|\.0*$/,'$1');
    this.mantise = split[1];
  }

  @Input()
  totalCells: number;

  part: string;
  mantise: string;
}
