class Human:
    name = None
    family = None
    hair_color = None    
    gender = None
    height = None

    # method - function
    def call(self):
        return f"{self.name} {self.family}"


p = Human()
p.name = 'Parham'
p.family = 'Javadi'
p.hair_color = 'black'
p.gender = 'm'
p.height = 170
print(p.call())
