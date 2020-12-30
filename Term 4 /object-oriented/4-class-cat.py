class Cat:
    origin = None
    color = None
    gender = None
    
    def sound(self):
        print(f'{self.origin} said Meow, Meow...')


p = Cat()
p.origin = 'Persian'
p.color = 'gray'
p.gender = 'female'
p.sound()