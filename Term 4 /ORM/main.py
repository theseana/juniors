from connection import Connection
from models import Student

session = Connection().create_session()
# CRUD

# Create
# person1 = Student('fatemeh', 'nasibipour', '2006-01-01', 98, 9)

# session.add(person1)
# session.commit()

# Read
persons = session.query(Student).filter(Student.first_name == 'mobin') 
for person in persons:
    print(person)


# Update


# Delete