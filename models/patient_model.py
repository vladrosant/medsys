from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    diagnosis = Column(String)

engine = create_engine('sqlite:///medical_system.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
