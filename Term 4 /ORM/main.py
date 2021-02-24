from connection import Connection
from models import Student

session = Connection().create_session()
# CRUD

# Create
# person1 = Student('fatemeh', 'nasibipour', '2006-01-01', 98, 9)

# session.add(person1)
# session.commit()

# Read
# persons = session.query(Student).filter(Student.first_name == 'mobin') 
# for person in persons:
#     print(person)


# Update
# person = session.query(Student).filter(Student.studentId == 1) 
# person.update({'first_name': 'hazhir'})
# session.commit()

# Delete
# person = session.query(Student).filter(Student.studentId == 1) 
# person.delete()
# session.commit()
