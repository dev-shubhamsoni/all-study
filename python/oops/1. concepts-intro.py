# class - is like a blueprint for creating objects, it defines what 
# attributes, data, methods,functions,behaviour that theobjects 
# created fomr this class will have

# Object is in instance of a class, think of it is an an exmaple created 

# Attributes are the variable that store the info about the object

# Methods are the functions defined inside the class

# self - n Python, self is the name used for the specific object a 
# method is working on. When you call a method on an object, Python 
# automatically passes that object in as the first argument, and by 
# convention that parameter is called self

class Dog:

    def __init__(self, name, breed, owner):
        # Attributes
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("woof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.contact_number = contact_number

owner1 = Owner("Shubham", "kaushal nagar", "888-999-000")
dog = Dog("tom", "rotwiler", owner1)

print(dog.owner.name)