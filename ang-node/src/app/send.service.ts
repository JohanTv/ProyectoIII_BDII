import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class SendService {

  constructor(private http: HttpClient) { }

  getAllPosts() {
    return this.http.get('/routes/send/').pipe(map((posts) => {
      return posts;
    }));
  }
}
