
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy import *
from sqlalchemy.dialects.mysql import LONGTEXT
from databasemodel import Patient


engine = create_engine('mysql+mysqldb://bd3121794ba1e4:6d936518@us-cdbr-iron-east-03.cleardb.net/heroku_e0771598287fecc')
connection = engine.connect()



Session = sessionmaker(engine)
session = Session()



data = {'first_name': 'ammar', 'last_name': 'ahmed'}
session.query(Patient).filter(Patient.patient_id==4).update(data)
session.commit()



