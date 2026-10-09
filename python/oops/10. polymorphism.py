# Polymorphism is one of the four main principles of OOP 
# (Object-Oriented Programming). It means one interface, 
# multiple forms.

# In Python, different classes can have methods with the same 
# name but implement them differently.

class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")


car = Car()
bike = Bike()

car.start()
bike.start()

# Polymorphism means the same method or interface can have different 
# behaviors depending on the object. Method overriding is one way to 
# achieve it.