
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


class LoginCredentials(Base):
    __tablename__ = 'login_credentials'
    
    id = Column(String(20), primary_key=True)
    password = Column(String(24), primary_key=True)


class DoctorLogin(Base):
    __tablename__ = 'doctor_logins'
    
    login_id = Column(Integer, primary_key=True, nullable=False)
    doctor_id = Column( Integer, ForeignKey("doctors.doctor_id"), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    status = Column(Integer, nullable=False)
    
    doctor = relationship("Doctor", back_populates = "doc_logins", uselist=False)

class PatientLogin(Base):
    __tablename__ = 'patient_logins'
    
    # one to one relationship (patient - login Credential)
    patient = relationship("Patient", back_populates = "logins", uselist=False)
    
    login_id = Column(Integer, primary_key=True, nullable=False)
    patient_id = Column(Integer,ForeignKey("patients.patient_id"),nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    status = Column(Integer, nullable=False)



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
    # one to many (Doctor - logins)
    doc_logins = relationship("DoctorLogin")


class Patient(Base):
    __tablename__ = 'patients'
    
    patient_id = Column(Integer, primary_key=True, nullable=False)
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
    # Defining a one to one relation (Patients - emergency contact)
    emergeny_C = relationship("EmergencyContact",uselist=False, back_populates="patient")
    # Defining a many to one relation pateint-doctor
    doctors = relationship("Doctor", foreign_keys=doctor_id)
    # Defining a one to one relation (Patients - health records)
    health_stats = relationship("Health_stats",uselist=False, back_populates="patient")
    #
    logins = relationship("PatientLogin")
    patients = relationship("PatientRecord")


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
    
    patient_id = Column(Integer,ForeignKey("patients.patient_id"),primary_key=True,nullable=False)
    contact_firstname = Column(String(20), nullable=False)
    contact_lastname = Column(String(20), nullable=False)
    relationship = Column(String(10), nullable=False)
    phone = Column(Integer, nullable=False)



class PatientRecord(Base):
    __tablename__ = 'patient_record'
    

    record_id = Column(Integer, primary_key=True)
    patient_id = Column(Integer,ForeignKey("patients.patient_id"),primary_key=True,nullable=False)
    blodd_pressure = Column(String(20), nullable=False)
    heart_rate = Column(String(20), nullable=False)
    weight = Column(String(10), nullable=False)
    created_on = Column(Integer, nullable=False)
    # Defining many to one relation
    patient = relationship("Patient", foreign_keys=patient_id)



#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

#mapp = inspect(Doctor)
#print(mapp)




