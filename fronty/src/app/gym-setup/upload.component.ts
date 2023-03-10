import { Component, OnInit } from '@angular/core';
//import {RequestService} from "../services/request-service/request.service";
import {take} from "rxjs/operators";
import {ActivatedRoute} from "@angular/router";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'uploader',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.scss']
})
export class UploadComponent implements OnInit {
  public readonly numberOfSteps: number = 1;
  public stepOne: number = 1;
  public currStep: number = 1;
  public form: FormGroup;

  constructor(//private requestService: RequestService,
              private activatedRoute: ActivatedRoute,
    private formBuilder: FormBuilder
              ) {
    this.form = formBuilder.group({

      "paper": [
        "",
        //"",
        []],
    })
  }

  public ngOnInit(): void {
    //We will use the gym org id to find all gyms which need setup, then set them upbased on their setupstate or w/e
    this.activatedRoute.data.subscribe((data) => {
      console.log(data)
    })
  }
  public stepOneContinue() {
    console.log(this.form.value)
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
