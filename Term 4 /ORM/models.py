from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column


Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    studentId = Column()
    name = Column()
    family = Column()
    grade = Column()
    created_at = Column()