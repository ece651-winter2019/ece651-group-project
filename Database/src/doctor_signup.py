
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy import *
from sqlalchemy.dialects.mysql import LONGTEXT
from databasemodel import Doctor


engine = create_engine('mysql+mysqldb://bd3121794ba1e4:6d936518@us-cdbr-iron-east-03.cleardb.net/heroku_e0771598287fecc')
connection = engine.connect()



Session = sessionmaker(engine)
session = Session()


doc = Doctor(
             first_name = "tong",
             last_name = "   ",
             email = "amme@gmail.com",
             phone_no = 4323791679,
             st = "32 king st s",
             city = "waterloo",
             state= "ON",
             postal_code = "N3L9f3",
            country = "Canada")


session.add(doc)
session.commit()
session.close()

