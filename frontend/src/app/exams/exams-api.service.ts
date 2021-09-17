import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from "rxjs";
import {catchError} from 'rxjs/operators';
import {API_URL} from '../env';
import {Exam} from './exam.model';
import {throwError as observableThrowError} from 'rxjs';

@Injectable()
export class ExamsApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: any): Observable<any> {
    return observableThrowError(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getExams(): Observable<any> {
    return this.http.get(`${API_URL}/exams`).pipe(catchError(ExamsApiService._handleError));
  }
}
