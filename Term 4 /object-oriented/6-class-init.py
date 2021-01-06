class Person:

    # __function    => magic
    # (d)ouble (under)line
    # dunder init 
    def __init__(self, n, f, a):
        self.name = n
        self.family = f 
        self.age = a

m = Person('mobin', 'ziyaie', 17)

print(m.family)