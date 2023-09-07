import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-list-adventures',
  templateUrl: './list-adventures.component.html',
  styleUrls: ['./list-adventures.component.css']
})
export class ListAdventuresComponent implements OnInit {

  adventures: any[] = [];

  // Inject HttpClient into your component or service.
  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    // Assuming you want to list adventures for user with ID 1. Adjust accordingly.
    const userId = 1;
    const apiUrl = `http://127.0.0.1:5000/list_adventures/${userId}`;

    this.http.get(apiUrl).subscribe((data: any) => {
      this.adventures = data;
    }, error => {
      console.error(error);  // Handle error response
    });
  }
}
