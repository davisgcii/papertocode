import { Component, OnInit } from '@angular/core';
//import {RequestService} from "../services/request-service/request.service";
import {take} from "rxjs/operators";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'UploaderComponent',
  templateUrl: './uploader.component.html',
  styleUrls: ['./uploader.component.scss']
})
export class UploaderComponent implements OnInit {
  public readonly numberOfSteps: number = 6;
  public stepOne: number = 1;
  public currStep: number = 1;


  constructor(//private requestService: RequestService,
              private activatedRoute: ActivatedRoute,
  ) { }

  public ngOnInit(): void {

  }
  public stepOneContinue() {
    if(this.stepOne < this.numberOfSteps) {
      this.stepOne++;
    } else {
      this.stepOne = 1
    }
    setTimeout(() => {
      if(this.currStep < this.numberOfSteps) {
        this.currStep++;
      } else {
        this.currStep = 1
      }
    }, 250);
  }
}
