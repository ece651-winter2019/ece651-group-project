import { Component, OnInit } from '@angular/core';
import { Patient } from '../patient';
import { PATIENTS } from '../mock-patients';

@Component({
  selector: 'app-patients',
  templateUrl: './patients.component.html',
  styleUrls: ['./patients.component.css']
})
export class PatientsComponent implements OnInit {

  patients = PATIENTS;

  patient: Patient = {
    id: 3,
    name: 'Peter',
    blood_p: 75,
    heart_r: 90
  }

  constructor() { }

  ngOnInit() {
  }

}
