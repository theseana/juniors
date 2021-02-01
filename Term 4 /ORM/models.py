from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, String, Date, TIMESTAMP
    )
from sqlalchemy.sql.functions import func
from connection import Connection

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    studentId = Column(Integer, primary_key=True, autoincrement=True) 
    first_name = Column(String(255))
    last_name = Column(String(255))
    birth_date = Column(Date)
    grade = Column(Integer)
    level = Column(Integer)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    )
    def __init__(self, f_n, l_n, b_d, g, l):
        self.first_name = f_n
        self.last_name = l_n
        self.birth_date = b_d
        self.grade = g
        self.level = l
    def __str__(self):
        return self.first_name +' '+ self.last_name

engine = Connection().get_connection()
Base.metadata.create_all(engine, checkfirst=True)