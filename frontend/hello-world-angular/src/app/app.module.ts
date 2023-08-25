import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { DataComponent } from './components/data.component';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent, DataComponent
  ],
  imports: [
    BrowserModule, HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent, DataComponent]
})
export class AppModule { }
