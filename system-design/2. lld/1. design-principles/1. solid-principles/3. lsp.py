"""
### Liskov Substitution Principle

LSP states: Objects of a parent class should be replaceable with objects of its child classes without breaking the 
expected behavior of the program.



"""

class Vehicle:
    def start_engine(self):
        print("Engine starting...")


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")


class Bicycle(Vehicle):
    def start_engine(self):
        raise NotImplementedError("Bicycles don't have engines")


print("Car:")
car = Car()
car.start_engine()

print("\nBicycle:")
bicycle = Bicycle()

try:
    bicycle.start_engine()
except NotImplementedError as e:
    print(f"Error: {e}")
    
    
"""

What's wrong?

Bicycle inherits from Vehicle, so code using a Vehicle reasonably expects start_engine() to work. 
But the bicycle throws an exception because it has no engine.

The child class cannot safely substitute for the parent in code that expects every Vehicle to start an engine.

Better approach: Separate capabilities
Not every vehicle has an engine. Keep the base class general and introduce a separate class for engine-powered vehicles.

"""
    
    
class Vehicle:
    def move(self):
        raise NotImplementedError


class MotorVehicle(Vehicle):
    def start_engine(self):
        print("Engine started.")


class Car(MotorVehicle):
    def move(self):
        print("Car is moving.")


class Bicycle(Vehicle):
    def move(self):
        print("Bicycle is moving.")


vehicles = [Car(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()