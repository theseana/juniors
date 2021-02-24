from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection:
    def __init__(self):
        self.engine = create_engine('mysql://poulstar:poulstar@localhost/club')

    def get_connection(self):
        return self.engine

    def create_session(self):
        Session = sessionmaker(bind=self.get_connection())
        return Session()