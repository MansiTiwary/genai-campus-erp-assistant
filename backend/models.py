# This file will define the SQLAlchemy ORM models.
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    enrollment_no = Column(String(20))
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    branch = Column(String(50))