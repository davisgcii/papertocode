import { Component, OnInit } from '@angular/core';
//import {RequestService} from "../services/request-service/request.service";
import {take} from "rxjs/operators";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'uploader',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.scss']
})
export class UploadComponent implements OnInit {
  public readonly numberOfSteps: number = 6;
  public stepOne: number = 1;
  public currStep: number = 1;


  constructor(//private requestService: RequestService,
              private activatedRoute: ActivatedRoute,
              ) { }

  public ngOnInit(): void {
    //We will use the gym org id to find all gyms which need setup, then set them upbased on their setupstate or w/e
    this.activatedRoute.data.subscribe((data) => {
      console.log(data)
    })
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
