import { Component, OnInit } from '@angular/core';
import {SendService} from '../send.service';

@Component({
  selector: 'app-send',
  templateUrl: './send.component.html',
  styleUrls: ['./send.component.css']
})
export class SendComponent implements OnInit {

  send: any = [];

  constructor(private sendService: SendService) { }

  ngOnInit() {
    this.sendService.getAllPosts().subscribe(send => {
        this.send = send;
    });
  }

}
