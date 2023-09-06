import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { DataComponent } from './components/data.component';
import { AppComponent } from './app.component';
import { AddAdventureComponent } from './components/add-adventure/add-adventure.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent, DataComponent, AddAdventureComponent
  ],
  imports: [
    BrowserModule, HttpClientModule, FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent, DataComponent]
})
export class AppModule { }
