class Cat:

    def __init__(self ,origin ,color ,gender):
        self.origin = origin
        self.color = color
        self.gender = gender
    
    def sound(self):
        print(f'{self.origin} said Meow, Meow...')
