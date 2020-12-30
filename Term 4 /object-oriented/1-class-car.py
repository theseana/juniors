class Car:
    # company, model, wheel, color, cross  => ویژگی - attribute
    company = None     
    model = None 
    wheel = None 
    color = None 
    cross = None 

p206 = Car()
# p206 >> object(شی) - instance(نمونه)
# Car >> class - کلاس
p206.company = 'Peugeot Fr'
p206.model = '206 t5'
p206.wheel = 4
p206.color = 'red'
p206.cross = False
print(f"p206 company is {p206.company}")
print(f"p206 color is {p206.color}")
print(f"p206 model is {p206.model}")
print(f"p206 wheel is {p206.wheel}")
print(f"p206 cross is {p206.cross}")
