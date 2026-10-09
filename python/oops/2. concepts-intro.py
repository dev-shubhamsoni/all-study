class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"hello my name is {self.name} and my age is {self.age} years old")
        
person1 = Person("Shuhbam", "26")
person1.greet()

person2 = Person("Ray", "32")
person2.greet()