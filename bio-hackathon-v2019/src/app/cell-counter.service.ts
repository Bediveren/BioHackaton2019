import {Injectable} from '@angular/core';
import {HttpClient, HttpEvent, HttpHeaders, HttpRequest} from "@angular/common/http";
import {Observable} from "rxjs";


const url = 'http://localhost:3000/upload';

@Injectable({
  providedIn: 'root'
})
export class CellCounterService {

  constructor(private http: HttpClient) {
  }

  count(image: File): Observable<any> {
    // create a new multipart-form for every file
    const formData: FormData = new FormData();
    formData.append('file', image, image.name);

    return this.http.post(url, formData);
  }
}

