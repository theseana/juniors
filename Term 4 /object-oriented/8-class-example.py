class Person:
    def __init__(self, name, family, birth_date):
        self.name = name
        self.family = family
        self.birth_date = birth_date

class Student(Person):
    def __init__(self, name, family, birth_date, grade):
        Person.__init__(self, name, family, birth_date)
        self.grade = grade

class Teacher(Person):
    def __init__(self, name, family, birth_date, degree, salary):
        Person.__init__(self, name, family, birth_date)
        self.degree = degree
        self.salary = salary

s = Teacher('mahan', 'kabir', '2000', 'B.S.', 5000)
a = Student('parha,', 'javadi', '2010', 20)
