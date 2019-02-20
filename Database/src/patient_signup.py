
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy import *
from sqlalchemy.dialects.mysql import LONGTEXT
from databasemodel import Patient, EmergencyContact


engine = create_engine('mysql+mysqldb://bd3121794ba1e4:6d936518@us-cdbr-iron-east-03.cleardb.net/heroku_e0771598287fecc')
connection = engine.connect()



Session = sessionmaker(engine)
session = Session()


patient = Patient(doctor_id = 2,
                  patient_id = 4,
             first_name = "ahmed",
             last_name = "ammar",
             dob = "1992-03-23",
             sex = "Male",
             height = "6,0",
             email = "ammarfa1993@gmail.com",
             phone_no = 4389791679,
             st = "32 king st s",
             city = "waterloo",
             state= "ON",
             postal_code = "N3L9f3",
            country = "Canada")

emergency_contact = EmergencyContact(
            patient_id = "4",
            contact_firstname = "omar",
            contact_lastname = "ahmed",
            relationship = "brother",
            phone = 234545435)

session.add(patient)
session.add(emergency_contact)
session.commit()


session.close()

