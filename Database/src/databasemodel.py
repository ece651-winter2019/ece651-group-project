
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import mapper, sessionmaker, relationship
from sqlalchemy import *
from sqlalchemy.dialects.mysql import LONGTEXT


engine = create_engine('mysql+mysqldb://bd3121794ba1e4:6d936518@us-cdbr-iron-east-03.cleardb.net/heroku_e0771598287fecc')


connection = engine.connect()
print(engine)
print(engine.table_names())


metadata = MetaData()
Base = declarative_base()
Session = sessionmaker(engine)


class Doctor(Base):
    __tablename__ = 'doctors'
    
    doctor_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column( String(20), nullable=False)
    last_name = Column( String(20), nullable=False)
    email = Column(String(20), nullable=False)
    phone_no = Column( Integer, nullable=False)
    st = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    state = Column( String(20), nullable=False)
    postal_code = Column( String(200000), nullable=False)
    country = Column(String(50), nullable=False)
    
    # Given an Doctor object a, we can now access patience associated to doctor using a.patients
    # Defining one to many relation Doctor-patient
    patients = relationship("Patient")
#patients = relationship("Patient", back_populates="doctor")



class Patient(Base):
    __tablename__ = 'patients'
    
    doctor_id = Column( Integer, ForeignKey("doctors.doctor_id"), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column( String(20), nullable=False)
    dob = Column( String(10), nullable=False)
    sex = Column( String(10), nullable=False)
    height = Column( String(6), nullable=False)
    email = Column(String(4294000000), nullable=False)
    phone_no = Column( BigInteger, nullable=False)
    st = Column( String(20), nullable=False)
    city = Column(String(20), nullable=False)
    state = Column( String(2), nullable=False)
    postal_code = Column( String(6), nullable=False)
    country = Column(String(50), nullable=False)
    patient_id = Column(Integer, primary_key=True, nullable=False)
    # Defining a one to one relation (Patients - emergency contact)
    emergeny_C = relationship("EmergencyContact",uselist=False, back_populates="patient")
    # Defining a one to one relation
    doctors = relationship("Doctor", foreign_keys=doctor_id)
    health_stats = relationship("Health_stats",uselist=False, back_populates="patient")
    #  emergeny_C = relationship("EmergencyContact", back_populates="patient")
#    logins = relationship("PatientLogin")

    def __repr__(self):
        return "<User(First name='%s', Last Name='%s', phone No='%s')>" % (
                                                                           self.first_name, self.last_name, self.phone_no)



class Health_stats(Base):
    __tablename__ = 'health_stats'
    
    record_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"),nullable=False)
    blood_pressure = Column(Integer, nullable=False)
    heart_rate = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    updated = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    # Defining a one to one relation
    patient = relationship("Patient", back_populates = "health_stats")


class EmergencyContact(Base):
    __tablename__ = 'emergency_contacts'
    
    # Defining a one to one relation
    patient = relationship("Patient", back_populates = "emergeny_C", uselist=False)
    
    contact_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer,ForeignKey("patients.patient_id"),nullable=False)
    contact_name = Column(String(20), nullable=False)
    relationship = Column(String(10), nullable=False)
    phone = Column(Integer, nullable=False)




#class PatientLogin(Base):
#    __tablename__ = 'patient_logins'
#
#    login_id = Column(Integer, primary_key=True, nullable=False)
#    email = Column(String(20) , ForeignKey("patients.email"), nullable=False)
#    created_on = Column(DateTime(), default=datetime.now)
#    status = Column(Integer, nullable=False)
#mysql_engine='InnoDB'


class DoctorLogin(Base):
    __tablename__ = 'doctor_logins'
    
    login_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(20), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    status = Column(Integer, nullable=False)
#mysql_engine='InnoDB'

class LoginCredentials(Base):
    __tablename__ = 'login_credentials'
    
    email = Column(String(20), primary_key=True)
    password = Column(String(24), primary_key=True)



Base.metadata.create_all(engine,  checkfirst=True)


mapp = inspect(Doctor)
print(mapp)




#session = Session()
#d = Doctor()
#d.doctor_id = 12
#d.first_name = "fdg"
#d.last_name = "rrfe"
#d.email = "ercwel"
#d.phone_no = 232
#d.st = "258B sunview st"
#d.city = "waterloo"
#d.state= "ON"
#d.postal_code = "N2L0H7"
#d.country = "Canada"
#
#session.add(d)
#
#p = Patient()
#p.patient_id = 0
#p.doctor_id = 12
#p.first_name = "Ammar"
#p.last_name = "Ahmed"
#p.dob = "09-06-1993"
#p.sex = "M"
#p.height = "5,7"
#p.email = "ammarfa"
#p.phone_no = 491679
#p.st = "258B sunview st"
#p.city = "waterloo"
#p.state= "ON"
#p.postal_code = "N2L0H7"
#p.country = "Canada"
#
#session.add(d)
#session.add(p)
#session.commit()
#
#session.close()


