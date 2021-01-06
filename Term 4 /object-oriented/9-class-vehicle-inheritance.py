class Vehicle:
    def __init__(self, model, fuel_cap, wheel):
        self.model = model
        self.fuel_cap = fuel_cap
        self.wheel = wheel

class Car(Vehicle):
    def __init__(self, model, fuel_cap, wheel, steer):
        Vehicle.__init__(self, model, fuel_cap, wheel)
        self.steer = steer
        

class Motor(Vehicle):
    def __init__(self, model, fuel_cap, wheel, jck):
        Vehicle.__init__(self, model, fuel_cap, wheel)
        self.jck = jck

s = Motor('Honda', '50', 2, True)
a = Car('Actyon', '80', 4, 'electonic')
