# Description of users' roles and basic user stories

## Basic set of users
* Patient
* Doctor
* System administrator

## Description os users' roles

* The patient wants to regularly upload his/her blood pressure measures into the system so the doctor can see them. Also, the user needs to see statistics of his/her own blood pressure measures over time. 
* The doctor aspires to regularly see the blood pressure patterns and statistics of each one of the patients.
* The system administrator is in charge of managing the entire system. It includes tasks such as adding/removing users and changing users’ roles and access permissions.

## Common user stories

### System administrator

1. Logs into the system through a web app using proper credentials.
2. Creates an account for a patient.
3. Creates an account for a doctor.
4. Deletes a patient account.
5. Deletes a doctor account.

### Doctor

1. Log into the system through a web app using proper credentials.
2. Look for one of the assigned patient’s by his/her last name.
3. For a particular patient, see the details of his/her last measure.
4. For a particular patient, see summary statistics over a period of time chosen by doctor (e.g. dd/mm/yyyy to dd/mm/yyyy)
5. See the rank of all the assigned patients sorted by their last measure.
6. See the rank of all the assigned patients sorted by their average measure over last week.
7. See the rank of all the assigned patients sorted by their average measure over last month.

### Patient

1. Log into the system through a mobile app using proper credentials.
2. Store measurement of his/her blood pressure in the database.
3. See the details of the last measure.
4. See summary statistics of the last week including a plot.
5. See summary statistics of the last month including a plot.
