# Inheritance in Python is an OOP concept where one class (child class) inherits attributes and 
# methods from another class (parent class).

# It helps you reuse code, extend existing functionality, and avoid duplication.

# - A car is a vehicle
# - A bike is a vehicle

class Vehicle:
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start(self):
        print("Vehicle is starting")
        
    def stop(self):
        print("vehicle is stopping")
        

class Car(Vehicle):
    def __init__(self,brand, model,year, no_of_doors):
        super().__init__(brand, model, year)
        self.doors = no_of_doors
        
car = Car("honda", "city", 2002, 4)
print(car.__dict__)
car.start()

# if we deine same method name as in aprent class than child
# method takes precedence