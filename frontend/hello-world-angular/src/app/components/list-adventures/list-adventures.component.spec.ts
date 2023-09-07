import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListAdventuresComponent } from './list-adventures.component';

describe('ListAdventuresComponent', () => {
  let component: ListAdventuresComponent;
  let fixture: ComponentFixture<ListAdventuresComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ListAdventuresComponent]
    });
    fixture = TestBed.createComponent(ListAdventuresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
