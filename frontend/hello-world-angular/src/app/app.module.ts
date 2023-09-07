import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { DataComponent } from './components/data.component';
import { AppComponent } from './app.component';
import { AddAdventureComponent } from './components/add-adventure/add-adventure.component';
import { FormsModule } from '@angular/forms';
import { ListAdventuresComponent } from './components/list-adventures/list-adventures.component';

@NgModule({
  declarations: [
    AppComponent, DataComponent, AddAdventureComponent, ListAdventuresComponent
  ],
  imports: [
    BrowserModule, HttpClientModule, FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent, DataComponent]
})
export class AppModule { }
