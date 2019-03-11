from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy import *
from sqlalchemy.dialects.mysql import LONGTEXT
from databasemodel import Doctor


engine = create_engine(
    "mysql+mysqldb://bd3121794ba1e4:6d936518@us-cdbr-iron-east-03.cleardb.net/heroku_e0771598287fecc"
)
connection = engine.connect()


Session = sessionmaker(engine)
session = Session()


delete_q = Doctor.__table__.delete().where(Doctor.doctor_id == "12")
session.execute(delete_q)
session.commit()


session.close()
