import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-add-adventure',
  templateUrl: './add-adventure.component.html',
  styleUrls: ['./add-adventure.component.css']
})
export class AddAdventureComponent implements OnInit {

  adventure = {
    date: '',
    category: '',
    mileage: null,
    estimated_calories: null
  };

  // Inject HttpClient into your component or service.
  constructor(private http: HttpClient) {}

  ngOnInit(): void {}

  onSubmit(): void {
    // Replace with your backend API endpoint
    const apiUrl = 'http://127.0.0.1:5000/add_adventure';
    this.http.post(apiUrl, this.adventure).subscribe(response => {
      console.log(response);  // Handle response from your backend API
    }, error => {
      console.error(error);  // Handle error response
    });
  }
}
