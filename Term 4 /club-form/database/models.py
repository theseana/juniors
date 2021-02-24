from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, Integer, String, Date, TIMESTAMP
    )
from sqlalchemy.sql.functions import func
from .connection import Connection

Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'
    member_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    image = Column(String(255))
    club_id = Column(Integer, unique=True)
    birth_date = Column(Date)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    )

    def __init__(self, first, last, image, birth, club_id):
       self.first_name = first
       self.last_name = last
       self.image = image
       self.birth_date = birth
       self.club_id = club_id
       # #################################################
       
    def __str__(self):
        return self.first_name +' '+ self.last_name

engine = Connection().get_connection()
Base.metadata.create_all(engine, checkfirst=True)