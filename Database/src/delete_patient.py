
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


delete_q = Patient.__table__.delete().where(Patient.patient_id == '4')
session.execute(delete_q)
session.commit()


session.close()

